# APPS
# ------------------------------------------------------------------------------
# from typing import Tuple

# ------------------------------------------------------------------------------
# BASE
# ------------------------------------------------------------------------------
DJANGO_APPS: tuple[str, ...] = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
)
THIRD_PARTY_APPS: tuple[str, ...] = (
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
)

LOCAL_APPS: tuple[str, ...] = (
    "site_dashboard.users",
    # Your stuff: custom apps go here
    # "site_dashboard.scraper",
    # "site_dashboard.scraping.crawler"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
