#!/usr/bin/python2.7
import re


def check_charge_value(f):
    def wrapp_checker(self, value):
        pattern_float = re.compile(r'[,.]{1}[\d]{0,2}')
        pattern_int = re.compile(r'[\d]+')
        match_float = re.search(pattern_float, str(value))
        match_int = re.search(pattern_int, str(value))
        result = ""
        if match_int:
            result = match_int.group()
        if match_float and len(match_float.group()) < 4:
            result += match_float.group()       
        if result == str(value):
            f(self, value)
        else:
            raise FormatException('incorrect charge format')
    return wrapp_checker


class Charge(object):
    @check_charge_value
    def __init__(self, value):
        self._value = float(value)
    value = property()
    
    @value.setter
    @check_charge_value
    def value(self, value):
        self._value = float(value)

    @value.getter
    def value(self):
        return self._value

    @value.deleter
    def value(self):
        self._value = None


class FormatException(Exception):
    pass

if __name__ == '__main__':
    while  True:
        try:
            value = raw_input()
            charge = Charge(value)
            print 'value in charge :: ' + str(charge.value)
        except Exception as e:
            print e.message