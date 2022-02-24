# images post telegram bot
Бот постит в канал изображения предварительно сохранённые с определённой периодичностью.
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
место сохранения и префикс названия файла.
### etch_images_from_url
Принимает список ссылок изображений, место сохранения и префикс названия файла.<br/>
Добавляет к названию файла суффикс - число, равное {количество файлов в images на момент сохранения} + 1.<br/>
Например *image_27.jpg*<br/>
Скачивает изображение и сохраняет его в указанную папку.
___
Код написан в образовательных целях на онлайн курсе по Python [dvmn.org](https://dvmn.org)





