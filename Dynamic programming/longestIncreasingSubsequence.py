"""
Longest Increasing Subsequence - Dynamic Programming

Time Complexity - O(n^2)
Space Complexity - O(n)
"""


def backtrack(dyn_ls,indices,ls):

    max_value = max(dyn_ls)
    max_index = dyn_ls.index(max_value)
    result = list()

    while max_index != -1:
        result.append(ls[max_index])
        max_index = indices[max_index]

    return result[::-1]


def longest_increasing_subseq(ls):

    dyn_ls = [1 for i in range(len(ls))]
    indices = [-1 for i in range(len(ls))]

    for i in range(len(ls)):
        for j in range(i):
            if ls[i] > ls[j]:
                if dyn_ls[j] + 1 > dyn_ls[i]:
                    indices[i] = j
                    dyn_ls[i] = dyn_ls[j] + 1

    return backtrack(dyn_ls,indices,ls)


                                ### Testcases ###
# print longest_increasing_subseq([3,4,-1,0,6,2,3])
