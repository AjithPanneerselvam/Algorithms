"""
Factors of a number

Time Complexity - O(sqrt(n))
Space Complexity - O(m), where m is the number of factors of a number
"""
from math import sqrt


def findFactors(n):
    if n == 1:
        return [1]

    factors = [1,n]

    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))

    return factors


#                               ### Test ###
print(findFactors(36))
print(findFactors(1))
print(findFactors(2))
