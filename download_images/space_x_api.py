import requests
import fetch_images_from_url


def get_urls_space_x_api():
    url_api_space_x = 'https://api.spacexdata.com/v4/launches/'
    response = requests.get(url_api_space_x)

    # Error handler
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])

    for launch_info in decoded_response:
        image_urls = launch_info['links']['flickr']['original']
        if image_urls:
            return image_urls


if __name__ == '__main__':
    path = 'images'
    names_prefix_image = 'image'
    urls_images = get_urls_space_x_api()
    fetch_images_from_url.fetch_images(urls_images, path, names_prefix_image)
