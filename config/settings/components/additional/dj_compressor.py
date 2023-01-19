# django-compressor
# ------------------------------------------------------------------------------
from config.settings.components.apps import INSTALLED_APPS
from config.settings.components.storage import STATICFILES_FINDERS

# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
INSTALLED_APPS += ("compressor",)
STATICFILES_FINDERS += ("compressor.finders.CompressorFinder",)
