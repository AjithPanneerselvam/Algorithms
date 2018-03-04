"""
Counting Sort
Time Complexity - O(n+k), where n is the input size and k is the range of input(maximum element in the input)
Space Complexity - O(n+k)
"""

def counting(ls):
    auxiliary = [0] * (max(ls) + 1)

    for i in range(len(ls)):
        auxiliary[ls[i]] += 1

    sorted_list = []
    for i in range(len(auxiliary)):
        if (auxiliary[i] > 0):
            for j in range(auxiliary[i]):
                sorted_list.append(i)

    return sorted_list


#                                ### Testcases ###
#
# ls = [4,3,1,7,8,5,2,19,15,100,95,125,11]
# print (counting(ls))
