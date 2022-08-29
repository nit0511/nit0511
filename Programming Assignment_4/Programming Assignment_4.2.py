#2. Write a Python Program to Display the multiplication Table?

import logging
logging.basicConfig(filename= "Programming Assignment_4.2.log", level= logging.DEBUG)

def Table(a):
    for b in range(2, a+1):
        for i in range(1, 11):

            print( b,"*", i ,"=", i*b)
            logging.info("%s * %s = %s", b,i, i*b)

Table(20)


