""" 
To check whether the m'th bit in an integer is set or not
"""

n = input()
m = input()
temp = 1 << (m-1)

if ((n and temp) == 0):
  print "m'th bit in {} is not set".format(n) 
else:
  print "m'th bit in {} is set".format(n) 
