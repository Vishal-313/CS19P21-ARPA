def PrimeNumber(num):
    if num == 0 or num == 1:
        return f"{num} is not a prime number"
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not a prime number"
        return f"{num} is a prime number"
