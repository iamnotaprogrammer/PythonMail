#!/usr/bin/python2.7


class FormatException(Exception):
    pass


class Charge(object):
   
    def __init__(self, value):
        try:
            self._value = round(float(value))
        except:
            raise FormatException('incorrect charge format')
    
    value = property()

    @value.setter
    def value(self, value):
        self._value = round(float(value))

    @value.getter
    def value(self):
        return self._value

    @value.deleter
    def value(self):
        self._value = None


class Account(object):
    def __init__(self, charge):
        self.charges = [charge,]
        self.total = charge.value
    
    def print_completed_charges(self):
        values = [str(charge.value) for charge in self.charges]
        print 'completed charges {0}'.format(' , '.join(values))
    
    def get_total(self):
        return self.total

    def add_trunsaction(self, charge):
        self.charges.append(charge)
        self.total += charge.value

if __name__ == '__main__':
    val = raw_input()
    charge = Charge(val)
    acc = Account(charge)
    while True:
        # try:
            val = raw_input()
            charge = Charge(val)
            acc.add_trunsaction(charge)
            acc.print_completed_charges()
            print acc.get_total()
        # except Exception as e:
        #     print str(e)



