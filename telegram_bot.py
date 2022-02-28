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

    image_names = os.listdir(path=path_current)
    random.shuffle(image_names)
    for filename in image_names:
        try:
            with open(f'{path_current}/{filename}', 'rb') as file:
                bot.send_photo(
                    chat_id=chat_id_group,
                    photo=file.read()
                )
            os.replace(
                f'{path_current}/{filename}',
                f'{path_destination}/{filename}'
            )
        except telegram.error.BadRequest:  # Если файл больше 15Мб
            os.replace(
                f'{path_current}/{filename}',
                f'{path_error}/{filename}'
            )
        sleep(publication_delay)


if __name__ == '__main__':
    main()
