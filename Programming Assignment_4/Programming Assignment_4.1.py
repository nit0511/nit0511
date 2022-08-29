1. Write a Python Program to Find the Factorial of a Number?

import logging
logging.basicConfig(filename= "Programming Assignment_4.1.log", level= logging.DEBUG)

def fac_num(a):
    logging.info("factorial of %s is being calculated", a)
    factorial = 1
    for i in range(1,a+1):
        factorial = factorial*i


    return factorial
factorial = fac_num(5)
print(factorial)
logging.info(factorial)



