import requests
import fetch_images_from_url


def get_urls_space_x_api():
    url_api_space_x = 'https://api.spacexdata.com/v4/launches/'
    response = requests.get(url_api_space_x)

    response.raise_for_status()

    for launch_info in response.json():
        url_roster = launch_info['links']['flickr']['original']
        if url_roster:
            return url_roster


if __name__ == '__main__':
    path = 'images'
    image_name_prefix = 'image'
    url_roster = get_urls_space_x_api()
    fetch_images_from_url.fetch_images(url_roster, path, image_name_prefix)
