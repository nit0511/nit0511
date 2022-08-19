#3. Write a Python program to display calendar?
import calendar
import logging
logging.basicConfig(filename= "Programming Assignment_2.3.log", level= logging.DEBUG)

yer = 2022
mon = 8
logging.info(calendar.month(yer,mon))
print(calendar.month(yer, mon))