# images post telegram bot
Бот постит в канал изображения предварительно сохранённые с определённой периодичностью.
___
### Настройка переменых окружения .env
**NASA_TOKEN**=*avVsX2sYBEdbOJ2hw9EZxlXAiTY88JFZS67fgsbV*</br>
[Сайт NASA APIs](https://api.nasa.gov/)

**TELEGRAM_BOT_TOKEN**=*5205777133:AAFTGuqxBgRm5UJ6mCt15ZgtYsqGXZwDnWg*</br>
[Получение API Bot Telegram](https://core.telegram.org/bots#6-botfather)

**CHAT_ID_BOT**=*376655992*</br>
**CHAT_ID_GROUP**=*-1002250619817*</br>
[Как узнать ID чата бота и чата группы.](https://lumpics.ru/how-find-out-chat-id-in-telegram/)

**PUBLICATION_DELAY**=*86400*</br>
Задержка публикации постов в секундах.
___

### telegram_bot
Постит канал (CHAT_ID_GROUP) изображения из папки images.<br/>
После отправки перемещает изображенив в папку images_shown.<br/>
Если изображение не удаётся отправить, перемещает его в папку error_image.<br/>
___

### download_images
Место для хранения папок с изображениями и скриптов для их получения и обработки.

### space_x_api, nasa_epic_api, nasa_adop_api
Делают запрос к API сайтов SpaceX и NASA.<br/>
После обработки передают *fetch_images_from_url* список ссылок изображений,<br/>
место сохранения и префикс названия файла.<br/>

Методы:<br/>
```
get_urls_space_x_api()
get_urls_nasa_epic_api()
get_urls_nasa_apod_api()
```

возвращают список с url изображений<br/>
```['https://apod.nasa.gov/apod/image/2202/NGC1555texas2021_1094.jpg', 'https://apod.nasa.gov/apod/image/2202/IC342Feller1024.jpg', ...]```

___
### fetch_images_from_url
Принимает список ссылок изображений, место сохранения и префикс названия файла.<br/>
Добавляет к названию файла суффикс - число, равное {количество файлов в images на момент сохранения} + 1.<br/>
Например *image_27.jpg*<br/>
Скачивает изображение и сохраняет его в указанную папку.
___
### Пример запуска
```
python telegram_bot.py
```
---
Код написан в образовательных целях на онлайн курсе по Python [dvmn.org](https://dvmn.org)





