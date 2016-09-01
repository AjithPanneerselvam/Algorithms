"""
To check whether a number is divisible by powers of 2
"""

number = input()

if number == 1:
    print "1 is divisble by 2^0"

# Working with bits will always makes your machine happy - O(1)
elif(not(number and number-1)):
    count = 0
    num =number
    while(num):
        num >>= 1
        count +=1
    print "The given number {} is divisible by 2^{}".format(number,count-1)

else:
    print "The given number {} is not divisible by 2^n".format(number)
