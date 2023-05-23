#Flask
SECRET_KEY = 'sdsds213123kldfklsd232'
   
# Flask-Mail
MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USERNAME = 'hello@ezbook.ru'
MAIL_PASSWORD = 'sicgyt-9zyxgy-nacceG'

#Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
