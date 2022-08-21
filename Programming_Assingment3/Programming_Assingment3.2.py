#2. Write a Python Program to Check if a Number is Odd or Even?

import logging
logging.basicConfig(filename="Programming_Assingment3.2.log", level= logging.DEBUG)

a = True
while a == True:
    try:
        number = float(input("please enter a number"))
        if number%2 == 0:
            print("Number is even")
            logging.info("Number is even and it is %s", number)

        else:
            print("Number is odd")
            logging.info("Number is odd and it is %s", number)
        a = False
    except:
        print("please enter valid input only")
        logging.info("please enter valid input only")