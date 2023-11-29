def fibonacci_sequence(n):
    if n < 0 or n == 0:
        print("")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
