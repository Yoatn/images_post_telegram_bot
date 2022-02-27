import requests
import fetch_images_from_url


def get_urls_space_x_api():
    url_api_space_x = 'https://api.spacexdata.com/v4/launches/'
    response = requests.get(url_api_space_x)

    # Error handler
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])

    for i in decoded_response:
        url_images = i['links']['flickr']['original']
        if url_images:
            return url_images
            break  # Чтобы получить только ссылки с последнего запуска.


if __name__ == '__main__':
    path = 'images'
    names_prefix_image = 'image'
    urls_images = get_urls_space_x_api()
    fetch_images_from_url.fetch_images(urls_images, path, names_prefix_image)
