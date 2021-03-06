"""
WSGI config for icode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icode.settings')

# attach debugger if on debug
# un-comment the code below to start vscode-debug

# if os.environ.get("DEBUG") or os.environ.get("WERKZEUG_RUN_MAIN"):
#     import ptvsd
#     ptvsd.enable_attach(address=('0.0.0.0', 8888))
#     print("Attached Remote Debugger")

application = get_wsgi_application()
