import requests
import os
from concurrent.futures import ProcessPoolExecutor


def download(item):
    date = item['date']
    media_type = item['media_type']
    url = item['url']

    if media_type == 'image':
        img_data = requests.get(url).content
        with open(f'nasa_media/{date}.jpg', 'wb') as f:
            f.write(img_data)
        print(f'Downloaded image for {date}')

    elif media_type == 'video':
        video_data = requests.get(url).content
        with open(f'nasa_media/{date}.mp4', 'wb') as f:
            f.write(video_data)
        print(f'Downloaded video for {date}')


if __name__ == '__main__':
    API_KEY = 'VYqpneaYgfDvGqNnfAtgXPQFJwAMOqHQdMjaWHNK'
    START_DATE = '2021-08-01'
    END_DATE = '2021-09-30'
    URL = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&start_date={START_DATE}&end_date={END_DATE}'

    os.makedirs('nasa_media', exist_ok=True)

    response = requests.get(URL)
    data = response.json()

    with ProcessPoolExecutor() as executor:
        executor.map(download, data)

    print('Download complete.')
