# -*- coding: utf-8 -*-
import os, sys

sys.path.insert(0, '/home/s/seoprovi/seoprovi.beget.tech/seoproject')
sys.path.insert(1, '/home/s/seoprovi/seoprovi.beget.tech/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'seoproject.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
