"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings
https://sobolevn.me/2017/04/managing-djangos-settings

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
import os

import django_stubs_ext
from split_settings.tools import include, optional

# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()

# Managing environment via `DJANGO_ENV` variable:
os.environ.setdefault("DJANGO_ENV", "local")
_ENV = os.environ["DJANGO_ENV"]

_base_settings = (
    "components/i18n.py",
    "components/db.py",
    "components/urls.py",
    "components/apps.py",
    "components/migration.py",
    "components/auth.py",
    "components/middleware.py",
    "components/storage.py",
    "components/templates.py",
    "components/security.py",
    "components/email.py",
    "components/admin.py",
    "components/logs.py",
    # 'components/celery.py',
    # 'components/dj_allauth.py',
    # 'components/dj_compressor.py',
    # 'components/drf.py',
    # 'components/corsheaders.py',
    "components/additional/celery.py",
    "components/additional/dj_allauth.py",
    "components/additional/dj_compressor.py",
    "components/additional/drf.py",
    "components/additional/corsheaders.py",
    # 'components/caches.py',
    # Select the right env:
    # f"environments/{_ENV}.py",
    # Optionally override some settings:
    optional(f"environments/{_ENV}.py"),
)

# Include settings:
include(
    *_base_settings,
    # optional('local.py'),
)
