import os
import requests


'''
Функция принимает список URL, адрес папки сох-ния и желаемое имя файла.
Добавляет к названию файла числовой индекс. Рашсирение считывает из URL.
Делает запрос по URL. Сохраняет полученные изображения в папку.
'''
def fetch_images(url_list, path='images', prefix='image'):
    if not os.path.exists(path):  # Проверяем есть ли такая папка.
        os.makedirs(path)  # Если нет, то создаём.
    # Проверяем сколько файлов в папке и +1. Это будет индекс следующего файла
    files_name_index = len(os.listdir(path=path)) + 1
    for url in url_list:
        filename = f'{prefix}_{files_name_index}{os.path.splitext(url)[1]}'
        response = requests.get(url)

        with open(f'{path}/{filename}', 'wb') as file:
            file.write(response.content)
        files_name_index += 1
