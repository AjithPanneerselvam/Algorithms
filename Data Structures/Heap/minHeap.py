"""
Minimum Heap

Time Complexity - O(log n)
Space Complexity - O(N)
"""

class MinHeap:
    def __init__(self):
        self.size = 0
        self.minHeap = ['#']


    def heapify(self):
        j = len(self.minHeap) - 1
        parent = int(j / 2)
        while(parent >= 1 and self.minHeap[parent] > self.minHeap[j]):
            self.minHeap[parent], self.minHeap[j] = self.minHeap[j], self.minHeap[parent]
            j = parent
            parent = int(parent / 2)


    def insert(self, data):
        self.minHeap.append(data)
        self.size = self.size + 1
        self.heapify()


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


    def percolateDown(self, index):
        while(index * 2 <= self.size):
            minChildIndex = self.minChildIndex(index)
            if self.minHeap[index] > self.minHeap[minChildIndex]:
                self.minHeap[index], self.minHeap[minChildIndex] = self.minHeap[minChildIndex], self.minHeap[index]
            index = minChildIndex


    def extractMin(self):
        if self.size == 0:
            return

        self.size = self.size - 1
        if self.size == 1:
            return self.minHeap.pop()
        minElement = self.minHeap[1]
        self.minHeap[1] = self.minHeap[-1]
        self.minHeap.pop()
        self.percolateDown(1)
        return minElement


    def peekMin(self):
        if self.size == 0:
            return
        return self.minHeap[1]


    def printHeap(self):
        if self.size == 0:
            return
        print (self.minHeap)


#                                 ### Testcases ###
heapObj = MinHeap()
heapObj.insert(9)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(3)
heapObj.insert(8)
heapObj.insert(7)
heapObj.insert(6)
heapObj.printHeap()
heapObj.insert(1)
heapObj.printHeap()
heapObj.insert(2)
heapObj.printHeap()
print (heapObj.extractMin())
heapObj.printHeap()
print (heapObj.peekMin())
