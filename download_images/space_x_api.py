import requests
import fetch_images_from_url


def main():
    path = 'images'  # Место сохранения фото
    names_prefix_image = 'image'
    # Создаём список с сылками на фото
    url_api_space_x = 'https://api.spacexdata.com/v4/launches/'
    response = requests.get(url_api_space_x)
    for i in response.json():
        url_images = i['links']['flickr']['original']
        if len(url_images) > 0:
            break  # Чтобы получить только ссылки с последнего запуска.
    fetch_images_from_url.fetch_images(url_images, path, names_prefix_image)


if __name__ == '__main__':
    main()