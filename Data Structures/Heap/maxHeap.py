"""
Maximum Heap

Time complexity - O(log n)
Space complexity - O(n)
"""

class MaxHeap:
    def __init__(self, listValues = []):
        self.size = 0
        # '#' represents that index 0 is invalid
        self.maxHeap = ['#']
        for val in listValues:
            self.maxHeap.append(val)
            self.size += 1
            self.percolateUp(self.size)


    def peekMax(self):
        if self.size == 0:
            return
        return self.maxHeap[1]


    def __str__(self):
        if self.size == 0:
            return
        return str(self.maxHeap)


    def maxChildIndex(self, index):
        if ((index * 2) + 1) <= self.size:
            if self.maxHeap[(index * 2) + 1] > self.maxHeap[index * 2]:
                return ((index * 2) + 1)
            elif self.maxHeap[(index * 2) + 1] < self.maxHeap[index * 2]:
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
        while(parent >= 1 and self.maxHeap[index] > self.maxHeap[parent]):
            self.maxHeap[index], self.maxHeap[parent] = self.maxHeap[parent], self.maxHeap[index]
            index = parent
            parent = int(parent / 2)


    def percolateDown(self, index):
        while(index * 2 <= self.size):
            maxChildIndex = self.maxChildIndex(index)
            if maxChildIndex != -1:
                if self.maxHeap[index] < self.maxHeap[maxChildIndex]:
                    self.maxHeap[index], self.maxHeap[maxChildIndex] = self.maxHeap[maxChildIndex], self.maxHeap[index]
            index = maxChildIndex


    def extractMax(self):
        if self.size == 0:
            return

        self.size = self.size - 1
        if self.size == 1:
            return self.maxHeap.pop()
        maxElement = self.maxHeap[1]
        self.maxHeap[1] = self.maxHeap[-1]
        self.maxHeap.pop()
        self.percolateDown(1)
        return maxElement


    def decreaseKey(self, index, newValue):
        if index >= 1 and index <= self.size:
            oldValue = self.maxHeap[index]
            self.maxHeap[index] = newValue
            if newValue > oldValue:
                self.percolateUp(index)
            elif newValue < oldValue:
                self.percolateDown(index)


    def insert(self, data):
        self.maxHeap.append(data)
        self.size = self.size + 1
        self.percolateUp(self.size)




#                                 ### Testcases ###
heapObj = MaxHeap()
heapObj.insert(9)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(3)
heapObj.insert(8)
heapObj.insert(7)
heapObj.insert(6)
print(heapObj)
heapObj.insert(11)
print(heapObj)
heapObj.insert(10)
print(heapObj)
print (heapObj.extractMax())
print(heapObj)
print (heapObj.peekMax())
heapObj.decreaseKey(2, 11)
print(heapObj)
heapObj.decreaseKey(3,5)
print(heapObj)
heapObj.decreaseKey(8,13)
print(heapObj)
