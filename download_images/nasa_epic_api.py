import requests
import fetch_images_from_url


def get_urls_nasa_epic_api():
    response = requests.get(
        'https://epic.gsfc.nasa.gov/api/natural/date/2015-10-31'
    )

    response.raise_for_status()

    url_roster = []
    for image_info in response.json():
        url_roster.append(
            # Здесь указываем .jpg т.к. целенаправленно берём файлы из папки /jpg
            f'https://epic.gsfc.nasa.gov/archive/natural/2015/10/31/jpg/{image_info["image"]}.jpg'
        )
    return url_roster


if __name__ == '__main__':
    path = 'images'
    image_name_prefix = 'image'
    url_roster = get_urls_nasa_epic_api()
    fetch_images_from_url.fetch_images(url_roster, path, image_name_prefix)
