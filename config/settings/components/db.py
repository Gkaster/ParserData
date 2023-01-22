# DATABASES / MIGRATIONS
# ------------------------------------------------------------------------------
# from config.settings.components import env
from config.settings.components import config

r"""
Local psql settings
# https://www.digitalocean.com/community/tutorials/
how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04

sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

sudo -u postgres psql
CREATE DATABASE site_dashboard;
CREATE USER debug WITH PASSWORD 'debug';
ALTER ROLE debug SET client_encoding TO 'utf8';
ALTER ROLE debug SET default_transaction_isolation TO 'read committed';
ALTER ROLE debug SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE site_dashboard TO debug;
\q

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myproject",
        "USER": "myprojectuser",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "",
    }
}


pycharm
HOST: localhost
DBMS: PostgreSQL (ver. 15.1 (Debian 15.1-1.pgdg110+1))
Case sensitivity: plain=lower, delimited=exact
Driver: PostgreSQL JDBC Driver (ver. 42.5.0, JDBC4.2)

Ping: 32 ms
SSL: yes
"""

# ------------------------------------------------------------------------------
# BASE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {"default": env.db("DATABASE_URL")}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('POSTGRES_DB', default='site_dashboard'),
#         'USER': env('POSTGRES_USER', default='debug'),
#         'PASSWORD': env('POSTGRES_PASSWORD', default='debug'),
#         'HOST': env('POSTGRES_HOST', default='postgres'),
#         'PORT': env.int('POSTGRES_PORT', default=5432),
#         'CONN_MAX_AGE': env.int('CONN_MAX_AGE', default=60),
#         'OPTIONS': {
#             'connect_timeout': 10,
#             'options': '-c statement_timeout=15000ms',
#         },
#     },
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="site_dashboard"),
        "USER": config("POSTGRES_USER", default="debug"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="debug"),
        "HOST": config("POSTGRES_HOST", default="postgres"),
        "PORT": config("POSTGRES_PORT", cast=int, default=5432),
        "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=60),
        "OPTIONS": {
            "connect_timeout": 10,
            "options": "-c statement_timeout=15000ms",
        },
    },
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
