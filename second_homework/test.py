#!/usr/bin/python3.5

import requests


if __name__ == '__main__':
    for el in range(10):
        res = requests.get(url='http://localhost:8082/')
        print('status code : %d' %res.status_code)
        print('body %s ' %res.text)
        