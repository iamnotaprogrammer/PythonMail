from django.conf.urls import url
from finance.views import hello_world
from finance.views import start
from finance.views import charges
from finance.views import transaction


urlpatterns = [
    url(r'^hello$', hello_world),
    url(r'^charges$', charges),
    url(r'^transactions$', transaction),
    url(r'^', start),
]
