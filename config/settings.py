DEBUG = True

SERVER_NAME = 'localhost:5000'
SECRET_KEY = b'<0\xdf\xf4\xe7\x8e\xccXT\xc7z\x02\xb4\x99\x04CW\rq\xc1;dET'


# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'abiliyok@gmail.com'
MAIL_PASSWORD = 'tiesan123'

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
