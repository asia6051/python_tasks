import os
import json
import xml.dom.minidom
import xml.etree.ElementTree as ET
from statistics import mean


def wrap_up_city(Temp: list, Wind: list):

    mean_temp = round(mean(Temp),2)
    max_temp, min_temp = round(max(Temp), 2), round(min(Temp), 2)
    mean_wind = round(mean(Wind), 2)
    max_wind, min_wind = round(max(Wind), 2), round(min(Wind), 2)

    dict_to_dump = {
        "mean_temp": str(mean_temp),
        "mean_wind_speed": str(mean_wind),
        "min_temp": str(min_temp),
        "min_wind_speed": str(min_wind),
        "max_temp": str(max_temp),
        "max_wind_speed": str(max_wind)
    }

    return dict_to_dump


def wrap_up_spain(Spain: dict):
    mean_temps = [values[0] for values in Spain.values()]
    mean_winds = [values[1] for values in Spain.values()]
    warmest = max(Spain, key=lambda city: Spain[city][0])
    coldest = min(Spain, key=lambda city: Spain[city][0])
    windiest = max(Spain, key=lambda city: Spain[city][1])

    mean_temp = round(mean(mean_temps), 2)
    mean_wind = round(mean(mean_winds), 2)

    dict_to_dump = {
        "mean_temp": str(mean_temp),
        "mean_wind_speed": str(mean_wind),
        "warmest_place": warmest,
        "coldest_place": coldest,
        "windiest_place": windiest
    }

    return dict_to_dump


if __name__ == '__main__':
    base_path = "source_data/{city}/2021_09_25.json"
    cities = os.listdir("source_data")

    # Creating root for xml file
    weather = ET.Element("weather", country="Spain", date="2021-09-25")
    cities_xml = ET.Element("cities")

    spain_stats = dict()


    # Iterating through all cities directories to find all json files
    for city_name in cities:
        city_path = base_path.format(city=city_name)

        if not os.path.isfile(city_path):
            continue

        with open(city_path, 'r') as file:
            json_data = json.load(file)

            curr_temp=[]
            curr_wind=[]

            for i in range(24):
                curr_temp.append(json_data['hourly'][i]['temp'])
                curr_wind.append(json_data['hourly'][i]['wind_speed'])

            # calculating city statistics
            city_numbers = wrap_up_city(curr_temp, curr_wind)

            # Correcting format of city tag and adding new city to xml tree
            city_name_corr = city_name.replace(' ', "_")
            city = ET.SubElement(cities_xml, city_name_corr, city_numbers)

            # adding city statistics to spain stats dict
            spain_stats[city_name_corr] = (float(city_numbers['mean_temp']), float(city_numbers['mean_wind_speed']))


    # calculating spain summary, adding it and cities summaries to xml
    spain_numbers = wrap_up_spain(spain_stats)
    summary = ET.SubElement(weather, "summary", spain_numbers)
    weather.append(cities_xml)

    # generating xml pretty string format and saving results
    xml_str = ET.tostring(weather)
    parsed_str = xml.dom.minidom.parseString(xml_str)
    pretty_xml_str = parsed_str.toprettyxml(indent="  ")

    with open('example_result.xml', 'w') as file:
        file.write(pretty_xml_str)
