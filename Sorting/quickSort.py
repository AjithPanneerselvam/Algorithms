"""
Merge sort:
Time Complexity - O(nlogn)
Space Complexity - O(1)
"""
import math
comparisons = 0


def quicksort(arr, left, right):
    global comparisons
    if left < right:
        comparisons += right - left
        pivotIndex = partition(arr, left, right)
        quicksort(arr, left, pivotIndex - 1)
        quicksort(arr, pivotIndex + 1, right)
        return arr


def partition(arr, left, right):

    ## Choosing median as the pivot element
    # pivotIndex = int(math.ceil((right+1+left)/2)) - 1

    ## Choosing first element as the pivot element
    pivotIndex = left

    ## Choosing last element as the pivot element
    # pivotIndex = right

    pivotValue = arr[pivotIndex]
    i = left

    for j in range(left, right + 1):
        if arr[j] < pivotValue:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[arr.index(pivotValue)], arr[i] = arr[i], arr[arr.index(pivotValue)]

    return i



									### Test Cases ###
ls = [2,1,4,8,7,5,3,12,6,10]
print (ls)
print (quicksort(ls, 0, len(ls) - 1))
print (comparisons)
