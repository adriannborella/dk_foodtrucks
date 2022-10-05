from .base import *
from .config.secure import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*,localhost').split(',')
