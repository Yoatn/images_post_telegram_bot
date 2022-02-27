import os
import random
from time import sleep
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()

    publication_delay = int(os.environ['PUBLICATION_DELAY'])
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id_group = os.environ["CHAT_ID_GROUP"]

    bot = telegram.Bot(token=telegram_bot_token)
    path_current = 'download_images/images'
    path_destination = 'download_images/images_shown'
    path_error = 'download_images/error_images'

    os.makedirs(path_destination, exist_ok=True)

    files_in_images = os.listdir(path=path_current)
    random.shuffle(files_in_images)
    for show_file in files_in_images:
        try:
            with open(f'{path_current}/{show_file}', 'rb') as file:
                bot.send_photo(
                    chat_id=chat_id_group,
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
        sleep(publication_delay)


if __name__ == '__main__':
    main()
