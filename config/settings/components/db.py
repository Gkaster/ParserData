# DATABASES / MIGRATIONS
# ------------------------------------------------------------------------------
# from config.settings.components import env
from config.settings.components import config

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
