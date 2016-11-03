import sys
import os
import random
import time
import datetime
from collections import namedtuple


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)

from my_modules import myfinance
from my_modules import html_make
from my_modules import date_value_generator

start_url = '/'
charges_page = '/charges'
charge = myfinance.Charge(100)
acc = myfinance.Account(charge)
Transaction = namedtuple("Transaction", ['date', 'value'])


def hello_world(request):
    return HttpResponse('<h1>Hello, World!</h1>')


def start(request):
    response = HttpResponse()
    response.write("<title>Home page</title>")
    response.write("<style> p { text-align:  center; }</style>")
    response.write("<div class = 'text'><p>WELCOM TO MY SITE !!!</p><div>")
    response.write("<p><a href='{0}'>Charges Page</a></p>".format(charges_page))
    return response


def charges(request):
    acc.add_trunsaction(myfinance.Charge(random.randrange(0, 100)))
    response = HttpResponse()
    response.write("<html><head>  <meta charset='utf-8'>")
    response.write('<p><b>CHARGE  PAGE</b></p>')
    response.write('<p><b>Total =  {0}</b></p>'.format(acc.total))
    response.write('{0}'.format(acc))
    response.write("<p><a href='{0}'><b>Start Page</b></a></p>".format(start_url))
    response.write("<head></html>")
    response.write(html_make.make_table())
    return response


def transaction(request):
    gen = date_value_generator.random_transaction()
    positive = list()
    negative = list()
    for date, value in gen:
        if value < 0:
            temp = Transaction(date=date, value=value)
            positive.append(temp)
        else:
            temp = Transaction(date=date, value=value)
            negative.append(temp)
    context = {
        'names': ['positive', 'negative'],
        'columns': ['Date', 'Value'],
        'transactions': {'positive': positive, 'negative': negative},
    }

    return render(request, 'finance/base.html', context)


