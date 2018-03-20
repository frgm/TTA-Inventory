import os
import sys
import django.core.handlers.wsgi

sys.path.append('/TTA_Inventory')
sys.path.append('/mainApp')

//os.environ['DJANGO_SETTINGS_MODULE'] = 'TTA_Inventory.settings'
application = django.core.handlers.wsgi.WSGIHandler()