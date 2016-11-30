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
from django.contrib.auth.models import User

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



def startpage(request):
    return render(request, 'finance/startpage.html')


def reg_user(request):
    if request.method == 'POST':
        user_form = forms.UserRegestrationForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user()
            user.username = request.POST['username'][0]
            user.password = request.POST['password'][0]
            user.first_name = request.POST['name'][0]
            user.last_name = request.POST['surname'][0]
            user.email = request.POST['email'][0]
            user.groups = 'User'
            user.user_permissions = request.POST['username'][0]
            user.is_staff = request.POST['username'][0]
            user.is_active = request.POST['username'][0]


            
            # user.save()
            # return HttpResponseRedirect('/auth')
    if request.method == 'GET':
        user_form = forms.UserRegestrationForm()
        context = {'title' : 'Create New User', 'form': user_form, 'path': request.path[1:]}
        return render(request, 'finance/registrations.html', context)
    return HttpResponseRedirect('/error')



def auth(request):
    if request.method == 'POST':
        acc_form = forms.AccountRegistrationForm(request.POST)
        if acc_form.is_valid():
            acc_form.save()
            return HttpResponseRedirect('/success')
    if request.method == 'GET':
        acc_form = forms.AccountRegistrationForm()
        context = {'title' : 'Create New Account', 'form': acc_form, 'path': request.path}
        return render(request, 'finance/acc_reg.html', context)
    return HttpResponseRedirect('/error')


def registration(request):
     if request.method == 'POST':
        acc_form = forms.AccountRegistrationForm(request.POST)
        if acc_form.is_valid():
            print(request.POST)
            # acc_form.save()
            # return HttpResponseRedirect('/success')
     if request.method == 'GET':
        acc_form = forms.AccountRegistrationForm()
        context = {'title' : 'Create New Account', 'form': acc_form, 'path': request.path}
        return render(request, 'finance/registrations.html', context)
     return HttpResponseRedirect('/error')


def show_accounts(request):
    pass


def homepage(request):
    return render(request, 'finance/base.html')


def start(request):
    response = HttpResponse()
    response.write("<title>Home page</title>")
    response.write("<style> p { text-align:  center; }</style>")
    response.write("<div class = 'text'><p>WELCOM TO MY SITE !!!</p><div>")
    response.write(
        "<p><a href='{0}'>Charges Page</a></p>".format(charges_page))
    return response


def charges(request):
    acc.add_trunsaction(myfinance.Charge(random.randrange(0, 100)))
    response = HttpResponse()
    response.write("<html><head>  <meta charset='utf-8'>")
    response.write('<p><b>CHARGE  PAGE</b></p>')
    response.write('<p><b>Total =  {0}</b></p>'.format(acc.total))
    response.write('{0}'.format(acc))
    response.write(
        "<p><a href='{0}'><b>Start Page</b></a></p>".format(start_url))
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
        if form.is_valid():
            return HttpResponseRedirect('/success')
    if request.method == 'GET':
        charge_form = forms.ChargeForm()
        context = {'form': charge_form}
        return render(request, 'finance/create_charges.html', context)
    return HttpResponseRedirect('/error')


def error_page(request):
    message = "It is the secret page. \
                You shouldn't talk anybody about it. I hope it will only our secret :))"
    context = {'message': message}
    return render(request, 'finance/error.html', context)


def good_answer(request):
    message = " Transaction well done!!!   \
                Sorry, but this app cannot work with database in this version: \
                Todo to develop database interface"
    context = {'message': message}
    return render(request, 'finance/succsess.html', context)
