def fun1():
    global a
    print a
    a = 1000


def fun2():
    global a
    print a


def fun3():
    global a
    print '333333333333333333333333'
    print a
    a = 100
    print a
    print '3333333333333333333333333'


def fun4():
    print a


a = 200

fun1()
fun2()
fun3()
fun4()
print a
