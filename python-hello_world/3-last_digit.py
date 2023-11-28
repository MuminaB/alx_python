import random
number = random.randint(-10000, 10000)
positive = number
if number < 0:
    positive = number * -1
    lastNumber = positive % 10
    if lastNumber != 0:
        lastNumber = lastNumber * -1
else:
    lastNumber = positive % 10

if lastNumber > 5:
    print("Last digit of {:d} is {:d}".format(number, lastNumber), end="")
    print(" and is greater than 5")
elif lastNumber < 6 and positive % 10 != 0:
    print("Last digit of {:d} is {:d}".format(number, lastNumber), end="")
    print(" and is less than 6 and not 0")
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastNumber))
       
