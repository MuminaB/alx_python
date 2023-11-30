def is_prime(number):
    if number <= 1:
        return False
    primeNumber = True
    if primeNumber:
        return True
    else:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
           
