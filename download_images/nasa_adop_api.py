import os
import requests
from dotenv import load_dotenv
from datetime import date, timedelta
import fetch_images_from_url

load_dotenv()

global NASA_TOKEN
NASA_TOKEN = os.environ['NASA_TOKEN']

payload = {
    'api_key': os.environ['NASA_TOKEN'],
    'start_date': f'{date(2022, 2, 10)}',  # Дата для > 30 снимков 2022-1-10
    # -1 день т.к. есть разница во времени локальном и сервера.
    'end_date': f'{date.today() - timedelta(days=1)}'
}

response = requests.get('https://api.nasa.gov/planetary/apod',
                        params=payload)

path = 'images'
names_prefix_image = 'image'
url_images = []
for i in response.json():
    if i['media_type'] == 'image':
        url_images.append(i['url'])

fetch_images_from_url.fetch_images(url_images, path, names_prefix_image)
