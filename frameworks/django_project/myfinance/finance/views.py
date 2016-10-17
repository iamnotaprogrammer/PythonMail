import sys
import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)
import random 
from  my_modules import myfinance
dir(myfinance)
# from myfinance import Account
# import myfinance



from django.shortcuts import render
from django.http import HttpResponse


start_url = 'localhost:8000'
charges_page = 'localhost:8000/charges'
charge = myfinance.Charge(100)
acc = myfinance.Account(charge)


def hello_world(request):
    return HttpResponse('<h1>Hello, World!</h1>')


def start(request):
    return HttpResponse("<p><a href='{0}'>Charges Page</a></p>".format(charges_page))


def charges(request):
    acc.add_trunsaction(myfinance.Charge(random.random()))
    response = HttpResponse()
    response.write('<p><b>CHARGE  PAGE</b></p>')
    response.write('<p><b>Total =  {0}</b></p>'.format(acc.total))
    response.write('{0}'.format(acc))
    response.write("<p><a href='{0}'>Start Page</a></p>".format(start_url))

    return response
