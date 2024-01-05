"""
ASGI config for myblog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import environ
from pathlib import Path

from django.core.asgi import get_asgi_application

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env読み込み
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

settings = env('DJANGO_PROJECT_NAME') + '.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

application = get_asgi_application()
