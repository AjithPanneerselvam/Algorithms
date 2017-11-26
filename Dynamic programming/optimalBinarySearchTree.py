"""
Optimal Binary Search Tree

Space-Complexity: O(n^2)
Reference: https://en.wikipedia.org/wiki/Optimal_binary_search_tree & http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/
"""

def optSearch(keys, frequency):
    # Intialize a temporary array, filled with zeroes
    dynArray = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        dynArray[i][i] = frequency[i]

    for diagonal in range(1, n):
        for row in range(n - diagonal):
            col = col + diagonal





                                ### Testcases ###
print(optSearch([10, 12, 20, 26],[11, 8, 50, 45]))
