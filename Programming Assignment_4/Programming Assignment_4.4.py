#4. Write a Python Program to Check Armstrong Number?
import logging
logging.basicConfig(filename= "Programming Assignment_4.4.log", level= logging.DEBUG)

def check_armstrong_no():
    logging.info("checking if no. is armstrong No.")
    d = True
    while d:
        try:
            a = int(input("please enter any number:"))
            c = str(a)
            b = 0
            for i in range(len(c)):
                b = int((c[i]))**len(c) + b
            if a == b:
                return 1,a
            else:
                return 0
            d = False

        except Exception as e:
            print("pleas enter a valid number", e)

b = check_armstrong_no()
print(b)

if b[0] == 1:
    print("no. is armstrong no. and it is ", b[1])
elif b == 0:
    print("no. is not an armstrong no.")
else:
    pass





