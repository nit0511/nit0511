#6. Write a Python Program to Find the Sum of Natural Numbers?

import logging
logging.basicConfig(filename= "Programming Assignment_4.6.log", level= logging.DEBUG)

a = int(input("please enter a number up to which you want sum of naturals nos."))
def sum_natural_no(a):
    b = 0
    for i in range(a):
        b = b + i

    return b
b = sum_natural_no(a)
logging.info("sum of %s natural no. is %s ",a,b)
print(b)