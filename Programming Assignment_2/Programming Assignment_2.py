#1. Write a Python program to convert kilometers to miles?

import logging
logging.basicConfig(filename= "Programming Assignment_2.log", level= logging.DEBUG)

a = True

while a == True:
    try:
        km = float(input("Enter the value of KM to convert it to miles"))
        miles = km * 0.621371192
        logging.info("%s KM is equals to %s", km, miles )
        print("%s KM is equals to %s", km, miles)
        a = False
    except Exception as e:
        logging.exception(e)
        logging.info("please enter only numerical value")


