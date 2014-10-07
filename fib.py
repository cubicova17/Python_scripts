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
    """Fibonachi number"""
    if x==1:
        return 1
    elif x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def fib2(x):
    """Making a list of fib x fib numbers"""
    l = [1,1]
    while len(l)<x:
        l.append(l[-1]+l[-2])
    return l

def main():
    print fib(7)
    print fib2(7)

if __name__ == '__main__':
    main()