"""
Base settings to build other settings files upon.
"""
from pathlib import Path

from decouple import AutoConfig

# import environ

# was before split settings
# ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# test in cmd:
# python3 -c "from pathlib import Path; print(Path('./__init__.py').resolve(strict=True).parent.parent.parent.parent)"
# BASE_DIR = Path(__file__).parent.parent.parent.parent
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
# site_dashboard/
APPS_DIR = ROOT_DIR / "site_dashboard"
# env = environ.Env()

# READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
# if READ_DOT_ENV_FILE:
#     # OS environment variables take precedence over variables from .env
#     env.read_env(str(ROOT_DIR / ".env"))

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
config = AutoConfig(search_path=ROOT_DIR.joinpath(".envs"))


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
# DEBUG = env.bool("DJANGO_DEBUG", False)
DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)
