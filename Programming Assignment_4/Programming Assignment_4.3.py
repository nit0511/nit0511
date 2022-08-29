#3. Write a Python Program to Print the Fibonacci sequence?

import logging
logging.basicConfig(filename= "Programming Assignment_4.3.log", level= logging.DEBUG)

def febonacci(a):
    try:
        first_digit =int(input("please enter first digit of febonacci series"))
        second_digit = int(input("please enter second digit of febonacci series"))
        logging.info("fibonacci sequence for where first and second element are %s and %s", first_digit, second_digit)
        print("febonacci sequence for ",first_digit, " and ", second_digit)
        febonacci_series = [first_digit, second_digit]
        for i in range(a-2):
            first_digit, second_digit = second_digit, second_digit+first_digit
            febonacci_series.append(second_digit)
    except Exception as e:
        print(e)

    return febonacci_series
b = febonacci(5)
print(b)
logging.info(b)

