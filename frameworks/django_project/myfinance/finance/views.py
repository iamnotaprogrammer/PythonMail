import sys
import os
import random
import time
import datetime

from django.shortcuts import render
from django.http import HttpResponse

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)

from  my_modules import myfinance

start_url = '/'
charges_page = '/charges'
charge = myfinance.Charge(100)
acc = myfinance.Account(charge)


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
    acc.add_trunsaction(myfinance.Charge(random.random()))
    response = HttpResponse()
    response.write("<html><head>  <meta charset='utf-8'>")
    response.write('<p><b>CHARGE  PAGE</b></p>')
    response.write('<p><b>Total =  {0}</b></p>'.format(acc.total))
    response.write('{0}'.format(acc))
    response.write("<p><a href='{0}'><b>Start Page</b></a></p>".format(start_url))
    response.write("<head></html>")
    response.write(make_table())
    return response


def mobile():
    return '8'+str(random.randrange(900, 999))+str(random.randrange(1000000, 9999999))


def name():
    return random.choice(['Ivan', 'Alexey', 'Geaorgiy', 'Artem'])


def lastname():
    return random.choice(['Smirnov', 'Nalbat', 'Tomphson', 'Tebenikov'])


def card():
    return str(random.randrange(1000, 9999)) + " "+str(random.randrange(1000, 9999)) + " "+str(random.randrange(1000, 9999)) \
    + " "+str(random.randrange(1000, 9999))


def date():
    cur_time = int(time.time())
    temp = 1000000
    datetime.datetime.fromtimestamp(random.randrange(cur_time-temp, cur_time))
    return datetime.datetime.fromtimestamp(random.randrange(cur_time-temp, cur_time)).strftime("%d-%m-%Y %H:%M:%S")


def make_table():
    table = "<table border=4>{0}</table>"
    caption = "<caption>{0}</caption>"
    thead = "<thead>{0}</thead>"
    tfoot = "<tfoot>{0}</tfoot>"
    tbody = "<tbody>{0}</tbody>"
    cell = "<td>{0}</td>"
    raw = "<tr>{0}</tr>"

    table_name = "MY RANDOM TABLE"
    columns = ["Date", 'Time', 'Name', 'Lastname', 'Mobile', 'User card number', 'Recipient']
    template = caption.format(table_name)+thead.format(make_raw(columns))
    raws = []
    for i in range(20):
        dat = date()
        values = [dat.split()[0], dat.split()[1], name(), lastname(), mobile(), card(), card()]
        raws.append(make_raw(values))

    tbody = tbody.format(''.join(raws))

    return table.format(template+tbody)


def make_raw(values):
    cell = "<td>{0}</td>"
    raw = "<tr>{0}</tr>"
    cells = []
    for el in values:
        cells.append(cell.format(el))
    return raw.format(''.join(cells))