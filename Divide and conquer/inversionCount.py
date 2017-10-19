"""
Inversion Count using Divide and Conquer
Time-Complexity - O(n log n), where n is the length of the array
Space-Complexity - O(n)
"""


def divide(A):
    n = len(A)
    if n > 1:
        leftHalf = A[:n/2]
        rightHalf = A[n/2:]
        x = divide(leftHalf)
        y = divide(rightHalf)
        z = splitInversion(A, leftHalf, rightHalf)
        return (x + y + z)
    return 0


def splitInversion(A, B, C):
    i = j = k = inversionCount = 0

    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A[k] = B[i]
            i += 1
        elif B[i] > C[j]:
            A[k] = C[j]
            j += 1
            inversionCount += len(B) - i
        else:
            A[k] = B[i]
            k += 1
            A[k] = B[i]
            i += 1
            j += 1
        k += 1

    # Copy the untouched elements of the array B to A
    while i < len(B):
        A[k] = B[i]
        k += 1
        i += 1

    # Copy the untouched elements of the array C to A
    while j < len(C):
        A[k] = C[j]
        k += 1
        j += 1

    return inversionCount


                                        ### Testcases ###
# A = [9,8,7,6,5,4]
# print divide(A), A
