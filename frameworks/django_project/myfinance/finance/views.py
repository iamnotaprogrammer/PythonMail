import sys
import os
import random
import time
import datetime
from collections import namedtuple


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader, Context

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)


import forms
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


def homepage(request):
    return render(request, 'finance/base.html')


# def new_charge(request):
#     charge_form = None
#     success = None

#     if request.method == 'POST':
#         charge_form = forms.ChargeForm(request.POST)
#         if charge_form.is_valid():
#             success = True
    
#     if request.method == 'GET':
#         charge_form = forms.ChargeForm()
#         success = False

#     context = {'form': charge_form}
#     return render(request, 'finance/create_charges.html', context)


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
        if value >= 0:
            temp = Transaction(date=date, value=value)
            positive.append(temp)
        else:
            temp = Transaction(date=date, value=value)
            negative.append(temp)
    context = {
        'columns': ['Date', 'Value'],
        'transactions': {'IN': positive, 'OUT': negative},
    }

    return render(request, 'finance/transactions.html', context)


def new_charge(request):
    if request.method == 'POST':
        form = forms.ChargeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            return HttpResponseRedirect('/success')
    if request.method == 'GET':
        charge_form = forms.ChargeForm()
        context = {'form': charge_form}
        return render(request, 'finance/create_charges.html', context)

    return HttpResponseRedirect('/error')


def error_page(request):
    message = "It is the secret page. \
                You shouldn'd talk anybody about it. I hope it will only our secret :))"
    context = {'message': message}
    return render(request, 'finance/error.html', context)


def good_answer(request):
    message = "Sorry, but this app cannot work with database in this version: \
        Todo to develop database interface"
    context = {'message': message} 
    return render(request, 'finance/succsess.html', context)