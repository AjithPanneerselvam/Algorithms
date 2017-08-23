"""
Selection sort
Time Complexity - O(n^2)
Space Complexity - O(1)
"""

def selection(ls):
    for i in range(len(ls)):
        minimum = ls[i]
        index = i
        for j in range(i+1,len(ls)):
            if minimum > ls[j]:
                index = j
                minimum = ls[j]
        ls[i],ls[index] = ls[index],ls[i]
    return ls


#                                 ### Testcases ###
#
# ls = [4,3,1,7,8,5]
# print (selection(ls))
