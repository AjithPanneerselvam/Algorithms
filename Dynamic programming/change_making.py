"""
Dynamic Programming - Change-making problem
Example: Given the coins with denomination [1,2,3]. Assume that there are infinite number of coins. Find the minimum number of coins to get the value 'x'.

Time Complexity - O(Total * Number of Coin Denominations)
Space Complexity - O(Total * Number of Coin Denominations)

Reference - https://en.wikipedia.org/wiki/Change-making_problem & http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""
from sys import maxint


def backtrack(matrix,denominations,target):
    j = target
    indices = list()

    for i in range(len(denominations), 0, -1):
        while matrix[i][j] != matrix[i-1][j]:
            indices.append(i-1)
            j = j - denominations[i-1]

    return indices


def change(denominations,target):
    matrix = [[0 for j in range(target + 1)] for i in range(len(denominations)+1)]

    for i in range(1,target+1):
        matrix[0][i] = maxint - 1

    for i in range(1,len(denominations)+1):
        for j in range(1,target+1):
            if denominations[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = min(matrix[i-1][j], 1 + matrix[i][j-denominations[i-1]])

    indices = backtrack(matrix, denominations, target)
    result_set = list()

    for i in indices:
        result_set.append(denominations[i])

    return result_set[::-1],matrix[len(denominations)][target]


                                ### Testcases ###
# print change([2,5,3,6],10)
# print change([1,2,3], 5)
