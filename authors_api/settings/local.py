from .base import *
from .base import env


DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="VoQE5G62Qu1Sk8cmBMa8V8D4nYhWazjaEoH9p9wWGPF4Pv23A3M68Wtme2BpHSwt",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

'django-insecure-ri*&9ecwc=k%m^gdbdqjc&_kb*lp*mv9fl*&_9-0-c-%o(k1g5'
