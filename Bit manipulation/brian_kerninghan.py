"""
Brian Kerninghan - Count the number of set bits in an integer
Time Complexity - O(log n)
Key idea: n & (n-1)
"""

def brian_kerninghan(n):
    count = 0
    while (n != 0):
        n = n & (n-1)
        count += 1
    return count

n = input()
print brian_kerninghan(n)
