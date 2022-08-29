a = input("please enter any number:")
length = len(a)

digit = []

for i in range(length):
    if i==0:
        dgt = int(a) % (10 * (i))

    print(f"{i+1}th digit is {dgt}")
'''
digits = []
for i in range(length+1):
    if not a[i].isnumeric():
        print("⚠️Not a Number")
    elif a[i].isnumeric():
        digits[i]=int(a[i])
    else:
        print("Unexpected Error")
'''

print(digits)