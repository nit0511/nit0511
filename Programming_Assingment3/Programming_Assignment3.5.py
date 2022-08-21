#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

import logging
logging.basicConfig(filename="Programming_Assingment3.5.log", level= logging.DEBUG)



b = []

for i in range(0, 10000):
    if i == 2 or i == 1:
       # logging.info(i)
        b.append(i)

    elif i%2 != 0 and i%3 != 0:
        #logging.info(i)
        b.append(i)

    else:
        pass
print(b)
logging.info(b)


