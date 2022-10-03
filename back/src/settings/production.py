from .base import *
from .config.secure import *

SECRET_KEY = os.environ.get('SECRET_KEY', '1321312')
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*,localhost').split(',')

CORS_ALLOWED_ORIGINS = ["<url_production>",]