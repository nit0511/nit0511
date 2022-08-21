#4. Write a Python Program to Check Prime Number?

import logging
logging.basicConfig(filename="Programming_Assingment3.4.log", level= logging.DEBUG)

a = True
while a == True:
    try:
        number = int(input("please enter a number: "))
        if number == 2 or number == 1:
            print("Number is prime")
            logging.info("Number is prime and it is %s", number)

        elif number%2 != 0 and number%3 != 0:
            print("Number is prime")
            logging.info("Number is prime and it is %s", number)

        else:
            print("Number is not a prime")
            logging.info("Number is not a prime and it is %s", number)

        a = False
    except:
        print("please enter valid input only")
        logging.info("please enter valid input only")