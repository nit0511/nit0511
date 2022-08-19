#2. Write a Python program to convert Celsius to Fahrenheit?
import logging
logging.basicConfig(filename= "Programming Assignment_2.2.log", level= logging.DEBUG)
a = True

while a == True:
    try:
        celcius = float(input("Enter the value of temperature in Celcius to convert it to Fahrenheit"))
        Fahrenheit = float(celcius * float(9/5)) + 32
        logging.info("%s celcius is equals to %s Fahrenheit", celcius, Fahrenheit )
        print(" value in Fahrenheit = ", Fahrenheit)
        a = False
    except Exception as e:
        logging.exception(e)
        logging.info("please enter only numerical value")

