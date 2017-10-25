"""
Sieve of Eratosthenes - Fastest algorithm to find all the prime numbers in a given range
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Prime Number - A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself

Time Complexity - O(n log(log n))
Space Complexity - O(n)
"""
from math import sqrt


def sieve(n):
    if n <= 1:
        return []

    primes = [1 for i in range(n+1)]
    primes[0] = primes[1] = 0

    for i in range(2, int(sqrt(n))+1):
        if primes[i]:
            j = 2
            while(i*j <= n):
                primes[i*j] = 0
                j += 1

    return primes


#                               ### Test ###
# print(sieve(40))
# print(sieve(0))
# print(sieve(1))
