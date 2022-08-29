#5. Write a Python Program to Find Armstrong Number in an Interval?


import logging
logging.basicConfig(filename= "Programming Assignment_4.5.log", level= logging.DEBUG)
logging.info("checking if no. is armstrong No.")

def check_armstrong_no(a):


    d = True
    while d:
        try:
            f = int(a)
            c = str(f)
            b = 0
            for i in range(len(c)):
                b = int((c[i]))**len(c) + b
            if f == b:
                return 1,f
            else:
                return 0
            d = False

        except Exception as e:
            print("pleas enter a valid number", e)

armstrong_no = []

for i in range(int(input("please enter a number up to which interval you want to get armstrong number"))):
    b = check_armstrong_no(i)
    try:
        if b[0] == 1:
            armstrong_no.append(b[1])
        else:
            pass
    except TypeError:
        pass
print(armstrong_no)
logging.info("list of all the armstrong numbers are %s", armstrong_no)






