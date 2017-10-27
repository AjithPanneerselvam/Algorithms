"""
Given an number, return the nearest power of 2
"""


def powerTwo(n):
    p = 1

    if n and (n & n -1) == 0:
        return n

    while p < n:
        p = p << 1

    return p


#                               ### Test ###
# print(powerTwo(7))
# print(powerTwo(82))
# print(powerTwo(16))
# print(powerTwo(0))
