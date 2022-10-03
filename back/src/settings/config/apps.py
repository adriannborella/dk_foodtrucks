DJANGO_APPS = [
    'material',  # https://pypi.org/project/django-material-admin/
    'material.admin',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",  # https://www.django-rest-framework.org/
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
    'rest_framework_simplejwt',
    "corsheaders",  # https://pypi.org/project/django-cors-headers/
]

LOCAL_APPS = [
    # "equality_proyect.users.apps.UsersConfig",
    # Your stuff: custom apps go here
    'apps.api',
    'apps.foodtracks'
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
