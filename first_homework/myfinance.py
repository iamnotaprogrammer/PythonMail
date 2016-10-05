#!/usr/bin/python2.7


class FormatException(Exception):
    pass


def my_round(f):
    def wrapper(value):
        return f(round(value, 2))
    return wrapper


@my_round
def printer(val):
    print val


class Charge(object):
   
    def __init__(self, value):
        try:
            self._value = round(float(value), 2)
        except:
            raise FormatException('incorrect charge format')
    
    def __str__(self):
        return str(self.value)

    value = property()

    @value.setter
    def value(self, value):
        self._value = round(float(value), 2)

    @value.getter
    def value(self):
        return self._value

    @value.deleter
    def value(self):
        self._value = None


class Account(object):
    def __init__(self, charge):
        self._charges = [charge,]
        self._total = charge.value

    def __str__(self):
        return "Account's Charges: {0}\n Total : {1}".format(', '.join(map(str, self.charges)), self.total)

    def __iter__(self):
        return iter(self.charges)

    @property
    def total(self):
        return self._total

    @property
    def charges(self):
        return self._charges

    def add_trunsaction(self, charge):
        self._charges.append(charge)
        self._total = max(self._total + charge.value, 0)


if __name__ == '__main__':
    val = raw_input()
    charge = Charge(val)
    acc = Account(charge)
    print acc    
    while True:
        val = raw_input()
        charge = Charge(val)
        acc.add_trunsaction(charge)
        print acc



