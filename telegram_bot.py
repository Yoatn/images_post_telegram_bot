import os
import random
from time import sleep
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()

    publication_delay = int(os.environ['PUBLICATION_DELAY'])
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    group_chat_id = os.environ["GROUP_CHAT_ID"]

    bot = telegram.Bot(token=telegram_bot_token)
    current_path = 'download_images/images'
    destination_path = 'download_images/images_shown'
    error_path = 'download_images/error_images'

    os.makedirs(destination_path, exist_ok=True)

    image_names = os.listdir(path=current_path)
    random.shuffle(image_names)
    for filename in image_names:
        try:
            with open(f'{current_path}/{filename}', 'rb') as file:
                bot.send_photo(
                    chat_id=group_chat_id,
                    photo=file.read()
                )
            os.replace(
                f'{current_path}/{filename}',
                f'{destination_path}/{filename}'
            )
        except telegram.error.BadRequest:  # Если файл больше 15Мб
            os.replace(
                f'{current_path}/{filename}',
                f'{error_path}/{filename}'
            )
        sleep(publication_delay)


if __name__ == '__main__':
    main()
