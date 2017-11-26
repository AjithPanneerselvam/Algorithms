"""
Dynamic Programming - Matrix chain multiplication

Time-Complexity - O(n^2); where n is the number of matrices
Space-Complexity - O(n^2)
Reference: https://en.wikipedia.org/wiki/Matrix_chain_multiplication & http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
"""

def matrixChainMultiplication(matricesDimension,n):
    # Intialize a temporary array, filled with zeroes
    dynArray = [[0 for j in range(n)] for i in range(n)]

    # Fill the array diagonally
    for diagonal in range(1,n):
        for row in range(n-diagonal):
            col = row + diagonal
            for c in range(row, col):
                result = dynArray[row][c] + dynArray[c+1][col]
                result += (matricesDimension[row] * matricesDimension[c+1] * matricesDimension[col+1])
                if result < dynArray[row][col] or dynArray[row][col] == 0:
                    dynArray[row][col] = result
    print(dynArray)
    return dynArray[0][n-1]


#                                                 ### Testcases ###
#
print(matrixChainMultiplication([2,3,6,4,5],4))
# print(matrixChainMultiplication([40,20,30,10,30],4))
# print(matrixChainMultiplication([10,20,30,40,30],4))
