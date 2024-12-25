import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = 'https://pl.wikipedia.org/wiki/Mariusz_Pudzianowski'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    print("\n\n=================================== PUDZILLA BRIEF ===================================\n")
    # basic info
    results = soup.find(id='content')
    box_elements = results.find_all("tr")

    for element in box_elements:
        element_title = element.find("th")
        element_value = element.find("p")

        if element_value and element_title:
            title = element_title.text.strip()
            value = element_value.text.strip()

            print(f"{title} : {value}\n")

    print("\n\n=================================== REKORDY PUDZILLI ===================================\n")
    # ultra pudzian info
    results2 = soup.find(id="mw-content-text")
    elements = results2.find_all("ul")
    records_elem = elements[12:14]

    for element in records_elem:
        list_items = element.find_all("li")

        for item in list_items:
            element_title = item.find("a")

            if element_title:
                title = element_title.text.strip()
                value = item.text.strip()
                print(f"{title} : {value}\n")
