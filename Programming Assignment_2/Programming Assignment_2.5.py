#5. Write a Python program to swap two variables without temp variable?
import logging
logging.basicConfig(filename= "Programming Assignment_2.5.log", level= logging.DEBUG)

a = 10
b = 20

logging.info("value of variable a and b are %s and %s before swapping", a , b)

a, b = b, a

logging.info("value of variable a and b are %s and %s after swapping", a , b)

