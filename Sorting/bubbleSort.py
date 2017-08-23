"""
Bubble sort
Time Complexity - O(n^2)
Space Complexity - O(1)
"""

def bubble(ls):
    for i in range(len(ls) -1):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1], ls[j]
    return ls


#                                 ### Testcases ###
#
# ls = [4,3,1,7,8,5]
# print (bubble(ls))
