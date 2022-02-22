import os
import random
from time import sleep
import telegram
from dotenv import load_dotenv

load_dotenv()

PUBLICATION_DELAY = int(os.environ['PUBLICATION_DELAY'])
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID_GROUP = os.environ["CHAT_ID_GROUP"]

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
path_current = 'download_images/images'
path_destination = 'download_images/images_shown'
path_error = 'download_images/error_image'

if not os.path.exists(path_destination):  # Проверяем есть ли такая папка.
    os.makedirs(path_destination)  # Если нет, то создаём.

while os.listdir(path=path_current):
    try:
        show_file = random.choice(os.listdir(path=path_current))
        with open(f'{path_current}/{show_file}', 'rb') as file:
            bot.send_photo(
                chat_id=CHAT_ID_GROUP,
                photo=file.read()
            )
        os.replace(
            f'{path_current}/{show_file}',
            f'{path_destination}/{show_file}'
        )
    except telegram.error.BadRequest:  # Если файл больше 15Мб
        os.replace(
            f'{path_current}/{show_file}',
            f'{path_error}/{show_file}'
        )
    sleep(PUBLICATION_DELAY)
