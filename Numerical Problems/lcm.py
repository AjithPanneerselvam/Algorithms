"""
Least Common Divisor
"""


def lcm(a,b,c):
    a = abs(a)
    b = abs(b)
    c = abs(c)

    lcm = max(a,b,c)
    startNumber = max(a,b,c)

    i = 2
    while(lcm%a != 0 or lcm%b != 0 or lcm%c != 0):

        lcm = startNumber * i
        i += 1

    return lcm


a,b,c = map(int, input().split(' '))
print(lcm(a,b,c))
