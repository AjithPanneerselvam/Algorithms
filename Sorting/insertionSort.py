"""
Insertion sort
Time Complexity - O(n^2)
Space Complexity - O(1)
"""

def insertion(ls):
    for i in range(len(ls)):
        temp = ls[i]
        j = i
        while(j > 0 and temp < ls[j-1]):
            ls[j] = ls[j-1]
            j -= 1
        ls[j] = temp
    return ls


#                                 ### Testcases ###
#
# ls = [4,3,1,7,8,5]
# print (insertion(ls))
