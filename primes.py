"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def checkPrime(numb):
    isPrime = True
    counter = 2
    if num == 1:
        isPrime = False
    else:
        while counter < num:
            if num % counter == 0:
                isPrime = False
            counter = counter + 1
    return isPrime 

def primes(number_of_primes):
    list = []
    currentNum = 1;
    while len(list) < number_of_primes:
        result = checkPrime(currentNum)
        if result == True:
            list.append(currentNum)
        currentNum = currentNum + 1
    return list

print(checkPrime(7))
print(primes(10))

