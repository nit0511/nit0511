#4. Write a Python program to solve quadratic equation?

import logging
logging.basicConfig(filename= "Programming Assignment_2.4.log", level= logging.DEBUG)

a = True
while a == True:
    try:
        a = float(input("Please enter the coefficient of x2"))
        b = float(input("Please enter the coefficient of x1"))
        c = float(input("Please enter the coefficient of x0"))

        x1 = (-(b) + (b**2-(4*a*c))**(1/2))/(2*a)
        x2 = ((b) + (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a)
        logging.info("solution of quadratic equation are %s and %s", x1, x2)
    except Exception as e:
        logging.info("please enter numerical value only")
        logging.info(e)
