"""
WSGI config for book_api_for_wookies_joolxk project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_api_for_wookies_joolxk.settings')

application = get_wsgi_application()
