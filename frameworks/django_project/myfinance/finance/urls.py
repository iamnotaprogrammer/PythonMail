from django.conf.urls import url
from finance.views import start
from finance.views import homepage
from finance.views import charges
from finance.views import transaction
from finance.views import good_answer
from finance.views import new_charge
from finance.views import error_page

urlpatterns = [
    url(r'^charges$', charges, name='charges'),
    url(r'^transactions$', transaction, name='transactions'),
    url(r'^newcharge$', new_charge, name='new_charge'),
    url(r'^success$', good_answer, name='success'),
    url(r'^error$', error_page, name='error_page'),
    url(r'^start', start, name='start_page'),
    url(r'^', homepage, name='homepage'),
]
