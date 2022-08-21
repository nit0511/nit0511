#3. Write a Python Program to Check Leap Year?

import logging
logging.basicConfig(filename="Programming_Assingment3.3.log", level= logging.DEBUG)

a = True
while a == True:
    try:
        number = int(input("please enter a number: "))
        if number % 100 == 0:
            if number%400 == 0:
                print("Year is leap year")
                logging.info("Year is leap year and it is %s", number)
            else:
                print("Year is not a leap year")
                logging.info("Year is not a leap year and it is %s", number)

        else:
            if number % 4 == 0:
                print("Year is leap year")
                logging.info("Year is leap year and it is %s", number)
            else:
                print("Year is not a leap year")
                logging.info("Year is not a leap year and it is %s", number)

        a = False
    except:
        print("please enter valid input only")
        logging.info("please enter valid input only")