"""
Maximum Heap

Time complexity - O(log n)
Space complexity - O(n)
"""

class MaxHeap:
    def __init__(self):
        self.size = 0
        # '#' represents that index 0 is invalid
        self.maxHeap = ['#']


    def heapify(self):
        """
        This method is used to preserve the Heap property by swapping elements.
        """
        j = len(self.maxHeap) - 1
        parent = int(j / 2)
        while(parent >= 1 and self.maxHeap[parent] < self.maxHeap[j]):
            self.maxHeap[parent], self.maxHeap[j] = self.maxHeap[j], self.maxHeap[parent]
            j = parent
            parent = int(parent / 2)


    def insert(self, data):
        self.maxHeap.append(data)
        self.size = self.size + 1
        self.heapify()


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


    def percolateDown(self, index):
        while(index * 2 <= self.size):
            maxChildIndex = self.maxChildIndex(index)
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


    def peekMax(self):
        if self.size == 0:
            return
        return self.maxHeap[1]


    def printHeap(self):
        if self.size == 0:
            return
        print (self.maxHeap)


#                                 ### Testcases ###
# heapObj = MaxHeap()
# heapObj.insert(9)
# heapObj.insert(5)
# heapObj.insert(4)
# heapObj.insert(3)
# heapObj.insert(8)
# heapObj.insert(7)
# heapObj.insert(6)
# heapObj.printHeap()
# heapObj.insert(11)
# heapObj.printHeap()
# heapObj.insert(10)
# heapObj.printHeap()
# print (heapObj.extractMax())
# heapObj.printHeap()
# print (heapObj.peekMax())
