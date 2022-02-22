import requests
import fetch_images_from_url

response = requests.get(
    'https://epic.gsfc.nasa.gov/api/natural/date/2015-10-31'
)
path = 'images'
names_prefix_image = 'image'
url_images = []
for i in response.json():
    url_images.append(
        # Здесь указываем .jpg т.к. целеноправлено берём файлы из папки /jpg
        f'https://epic.gsfc.nasa.gov/archive/natural/2015/10/31/jpg/{i["image"]}.jpg'
    )

fetch_images_from_url.fetch_images(url_images, path, names_prefix_image)
