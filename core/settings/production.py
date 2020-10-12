from . import *


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


sentry_sdk.init(
    dsn="https://27f46d50dc964cf384b2a9d6dc63c20a@o449328.ingest.sentry.io/5432078",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=False,
    debug=True,
)


SECRET_KEY = "dev1%3kz*2vvcv_m41@t0%tz6fyq**d_79c^jpx4g&b9@ypeyp*wwdev"

DEBUG = False

ALLOWED_HOSTS = ["46.101.138.175"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "purdb",
        "USER": "projectuser",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
