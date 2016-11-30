from django.conf.urls import url
from finance.views import start
from finance.views import homepage
from finance.views import charges
from finance.views import transaction
from finance.views import good_answer
from finance.views import new_charge
from finance.views import error_page
from finance.views import show_accounts
from finance.views import registration
from finance.views import reg_user
from finance.views import auth
from finance.views import startpage

urlpatterns = [
    url(r'^charges$', charges, name='charges'),
    url(r'^transactions$', transaction, name='transactions'),
    url(r'^newcharge$', new_charge, name='new_charge'),
    url(r'^success$', good_answer, name='success'),
    url(r'^error$', error_page, name='error_page'),
    # url(r'^start$', start, name='start_page'),
    url(r'^registration$', registration, name='registration'),
    url(r'^reg_user$', reg_user, name='reg_user'),
    url(r'^auth$', auth, name='auth'),
    url(r'^start$', startpage, name='startpage'),
    url(r'^', homepage, name='homepage'),

]
