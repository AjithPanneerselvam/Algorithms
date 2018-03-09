"""
Heap Sort

Time Complexity - O(nlogn)
Space Complexity - O(n)
"""

from heapq import _heapify_max

def heapSort(arr):
    
    resultArr = [0] * len(arr)
    n = len(arr) - 1

    while(n != 0):
        _heapify_max(arr)
        resultArr[n] = arr[0]
        arr[0], arr[n] = arr[n], arr[0]
        arr.pop()
        n -= 1
    
    resultArr[n] = arr[0]
    print(resultArr)


arr = [11, 23, 41, 2, 3]
heapSort(arr)