#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

import logging
logging.basicConfig(filename="Programming_Assingment3.1.log", level= logging.DEBUG)

a = True
while a == True:
    try:
        number = float(input("please enter a number"))
        if number < 0:
            print("Number is negative")
            logging.info("Number is negative and it is %s", number)

        elif number > 0:
            print("Number is positive")
            logging.info("Number is positive and it is %s", number)

        else:
            print("Number is Zero")
            logging.info("Number is Zero")
        a = False
    except:
        print("please enter valid input only")
        logging.info("please enter valid input only")


