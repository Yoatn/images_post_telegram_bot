from os import environ
import requests
from dotenv import load_dotenv
from datetime import date, timedelta
import fetch_images_from_url


def get_urls_nasa_apod_api():
    load_dotenv()

    payload = {
        'api_key': environ['NASA_TOKEN'],
        'start_date': f'{date(2022, 2, 10)}',  # Дата для > 30 снимков 2022-1-10
        # -1 день т.к. есть разница во времени локальном и сервера.
        'end_date': f'{date.today() - timedelta(days=1)}'
    }
    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params=payload)

    response.raise_for_status()

    url_images = []
    for i in response.json():
        if i['media_type'] == 'image':
            url_images.append(i['url'])

    return url_images


if __name__ == '__main__':
    path = 'images_1'
    names_prefix_image = 'image'
    urls_images = get_urls_nasa_apod_api()
    fetch_images_from_url.fetch_images(urls_images, path, names_prefix_image)
