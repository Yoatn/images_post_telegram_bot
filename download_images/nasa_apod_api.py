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

    url_roster = []
    for image_info in response.json():
        if i['media_type'] == 'image':
            url_roster.append(image_info['url'])

    return url_roster


if __name__ == '__main__':
    path = 'images'
    image_name_prefix = 'image'
    url_roster = get_urls_nasa_apod_api()
    fetch_images_from_url.fetch_images(url_roster, path, image_name_prefix)
