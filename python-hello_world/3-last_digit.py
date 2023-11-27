import random
number = random.randint(-10000, 10000)

if number < 0:
    number = number * 1
    lastNumber = number % 10
    if lastNumber != 0:
        lastNumber = lastNumber * -1
else:
    lastNumber = number % 10

if lastNumber > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, lastNumber), end="")
elif lastNumber < 6 and number % 10 != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, lastNumber), end="")
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastNumber))
      
