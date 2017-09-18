"""
Minimum Heap

Time Complexity - O(log n)
Space Complexity - O(N)
"""

class MinHeap:
    def __init__(self, listValues = []):
        self.size = 0
        self.minHeap = ['#']
        for val in listValues:
            self.minHeap.append(val)
            self.size += 1
            self.percolateUp(self.size)


    def peekMin(self):
        if self.size == 0:
            return
        return self.minHeap[1]


    def __str__(self):
        if self.size == 0:
            return
        return str(self.minHeap)


    def minChildIndex(self, index):
        if ((index * 2) + 1) <= self.size:
            if self.minHeap[(index * 2) + 1] < self.minHeap[index * 2]:
                return ((index * 2) + 1)
            elif self.minHeap[(index * 2) + 1] > self.minHeap[index * 2]:
                return (index * 2)
            else:
                # return any node, if both the children has same value
                return (index * 2)
        elif (index * 2) <= self.size:
            return (index * 2)
        else:
            # No children for the given Node
            return (-1)


    def percolateUp(self, index):
        parent = int(index / 2)
        while(parent >= 1 and self.minHeap[parent] > self.minHeap[index]):
            self.minHeap[parent], self.minHeap[index] = self.minHeap[index], self.minHeap[parent]
            index = parent
            parent = int(parent / 2)


    def percolateDown(self, index):
        while(index * 2 <= self.size):
            minChildIndex = self.minChildIndex(index)
            if self.minHeap[index] > self.minHeap[minChildIndex]:
                self.minHeap[index], self.minHeap[minChildIndex] = self.minHeap[minChildIndex], self.minHeap[index]
            index = minChildIndex


    def extractMin(self):
        if self.size == 0:
            return
        self.size -= 1
        if self.size == 1:
            return self.minHeap.pop()
        minElement = self.minHeap[1]
        self.minHeap[1] = self.minHeap[-1]
        self.minHeap.pop()
        self.percolateDown(1)
        return minElement


    def decreaseKey(self, index, newValue):
        oldValue = self.minHeap[index]
        self.minHeap[index] = newValue
        if newValue < oldValue:
            self.percolateUp(index)
        elif newValue > oldValue:
            self.percolateDown(index)


    def insert(self, data):
        self.minHeap.append(data)
        self.size += 1
        self.percolateUp(self.size)


#                                 ### Testcases ###
heapObj = MinHeap([9,5,4,3,8,7,6])
print(heapObj)
heapObj.insert(1)
print(heapObj)
heapObj.insert(2)
print(heapObj)
print (heapObj.extractMin())
print(heapObj)
print (heapObj.peekMin())
heapObj.decreaseKey(4,1)
print(heapObj)
heapObj.decreaseKey(2,11)
print(heapObj)
