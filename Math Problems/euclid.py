"""
Euclid Algorithm

Time Complexity - O(n), where n is the number of digits in b, where b < a
Space Complexity - O(1)
"""


def gcd(a,b):

    while(b != 0):
        temp = a
        a = b
        b = temp % b

    return a


def recursiveGCD(a,b):
    return a if b == 0 else recursiveGCD(b, a % b)


#                           ### Test ###
# print(gcd(16,8))
# print(gcd(66,55))
# print(recursiveGCD(66,55))
