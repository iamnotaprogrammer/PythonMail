from django.conf.urls import url
from finance.views import hello_world
from finance.views import start
from finance.views import charges

urlpatterns = [
    url(r'^hello$', hello_world),
    url(r'^charges$', charges),
    url(r'^', start),
]
