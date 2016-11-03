import sys
import os
import random
import time
import datetime
from collections import namedtuple


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)

from my_modules import myfinance
from my_modules import html_make
from my_modules import date_value_generator


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


def mobile():
    return '8'+str(random.randrange(900, 999))+str(random.randrange(1000000, 9999999))


def name():
    return random.choice(['Ivan', 'Alexey', 'Geaorgiy', 'Artem'])


def lastname():
    return random.choice(['Smirnov', 'Nalbat', 'Tomphson', 'Tebenikov'])


def card():
    return str(random.randrange(1000, 9999)) + " "+str(random.randrange(1000, 9999)) + " "+str(random.randrange(1000, 9999)) \
    +" "+str(random.randrange(1000, 9999))


def date():
    cur_time = int(time.time())
    temp = 1000000
    datetime.datetime.fromtimestamp(random.randrange(cur_time-temp, cur_time))
    return datetime.datetime.fromtimestamp(random.randrange(cur_time-temp, cur_time)).strftime("%d-%m-%Y %H:%M:%S")