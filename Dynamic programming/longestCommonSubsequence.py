"""
Dynamic Programming - Longest Common Subsequence
Find the longest common Subsequence between two strings.

Input:
    Strings -> s1 and s2

Time Complexity - O(len1 * len2), where len1 and leng2 are the length of the given Strings s1 and s2 respectively.
Space Complexity - O(len1 * len2)
Reference - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""

def backtrack(dyn_array,len1,len2):
    j = len2
    indices = list()

    for i in range(len1,0,-1):
        if dyn_array[i][j] == dyn_array[i-1][j-1] + 1:
            indices.append(i-1)
            j -= 1
        else:
            if dyn_array[i-1][j] == dyn_array[i][j-1]:
                continue
            elif dyn_array[i][j] == dyn_array[i-1][j]:
                continue
            else:
                j -= 1

    return indices


def lcs(s1,s2):
    dyn_array = [[0] for i in range(len(s1)+1)]

    for i in range(len(s2)):
        dyn_array[0].append(0)

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dyn_array[i].append(dyn_array[i-1][j-1] + 1)
            else:
                dyn_array[i].append(max(dyn_array[i][j-1],dyn_array[i-1][j]))

    indices = backtrack(dyn_array, len(s1), len(s2))
    longest_common_subsequence = list()

    for i in indices:
        longest_common_subsequence.append(s1[i])

    return longest_common_subsequence[::-1], dyn_array[len(s1)][len(s2)]


                                ### Testcases ###
# print lcs("abcdef","zagcemf")
