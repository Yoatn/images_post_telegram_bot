import requests
import fetch_images_from_url


def get_urls_nasa_epic_api():
    response = requests.get(
        'https://epic.gsfc.nasa.gov/api/natural/date/2015-10-31'
    )

    response.raise_for_status()

    urls_images = []
    for i in response.json():
        urls_images.append(
            # Здесь указываем .jpg т.к. целенаправленно берём файлы из папки /jpg
            f'https://epic.gsfc.nasa.gov/archive/natural/2015/10/31/jpg/{i["image"]}.jpg'
        )
    return urls_images


if __name__ == '__main__':
    path = 'images'
    names_prefix_image = 'image'
    urls_images = get_urls_nasa_epic_api()
    fetch_images_from_url.fetch_images(urls_images, path, names_prefix_image)
