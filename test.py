import time
import datetime
import random


def case(var, defult, dic=None, **kw):
    if not dic is None:
        if str(type(dic)) == "<class 'dict'>":
            vars = dic.keys()
            if var in vars:
                dic[var]()
            else:
                defult()
    else:
        vars = kw.keys()
        if var in vars:
            kw[var]()
        else:
            defult()


def tt():
    print(True)
    return True


def ff():
    print(False)
    return False


def my_print(var):
    print(var, type(var), sep='\n')


flag = False
for i in range(50000):
    a = random.randint(0, 2)
    print(a)
    case(a, lambda x=(datetime.datetime.fromtimestamp(time.time())): my_print(x), {0: tt, 1: ff})
    if a == 0:
        flag = True
        print(i)
        break


