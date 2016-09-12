""" 
To check whether the m'th bit in an integer is set or not
"""

n = input()
m = input()
temp = 1 << (m-1)

if ((n and temp) == 0):
  print "not set" 
else:
  print "set"
