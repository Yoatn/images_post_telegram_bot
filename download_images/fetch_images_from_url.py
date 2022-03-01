import os
import requests

'''
Функция принимает список URL, адрес папки сох-ния и желаемое имя файла.
Добавляет к названию файла числовой индекс. Рашсирение считывает из URL.
Делает запрос по URL. Сохраняет полученные изображения в папку.
'''


def fetch_images(url_roster, path='images', prefix='image'):
    os.makedirs(path, exist_ok=True)
    # Проверяем сколько файлов в папке и +1. Это будет индекс следующего файла
    file_name_index = len(os.listdir(path=path)) + 1
    for url in url_roster:
        filename = f'{prefix}_{file_name_index}{os.path.splitext(url)[1]}'
        response = requests.get(url)

        response.raise_for_status()

        with open(f'{path}/{filename}', 'wb') as file:
            file.write(response.content)
        file_name_index += 1
