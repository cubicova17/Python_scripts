#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dvoiak
#
# Created:     07.10.2014
# Copyright:   (c) Dvoiak 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def fib(x):
    """Recursive Fibonachi number"""
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

def fib2(x):
    """Making a list of "x" fib numbers (no recursion)"""
    l = [0,1]
    while len(l)<x:
        l.append(l[-1]+l[-2])
    return l

def fib3(x):
    """dfd"""
    a = 0
    b = 1
    for i in range(x-2):
        a,b = b,a+b
    return b

def main():
    N = 7
    print fib(N)
    print fib2(N)
    print fib3(N)

if __name__ == '__main__':
    main()