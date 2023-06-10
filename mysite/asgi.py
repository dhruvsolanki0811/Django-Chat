import os
from .wsgi import *  # add this line to top of your code
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chatapp import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myApp.settings')
import django
django.setup()



application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
})