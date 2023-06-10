import os, django

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chatapp import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myApp.settings')
django.setup()
django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
})