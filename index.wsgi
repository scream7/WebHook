import sae
from WebHook import wsgi

application = sae.create_wsgi_app(wsgi.application)