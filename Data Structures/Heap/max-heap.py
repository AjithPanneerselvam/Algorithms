"""
Maximum Heap
"""

class BinaryHeap:
    def __init__(self, size = 0):
        self.size = size
        # '#' represents that index 0 is invalid
        self.heap = ['#']


    def insert(self, data):
        self.heap.append(data)
        self.size = self.size + 1
        self.heapify()


    def heapify(self):
        j = len(self.heap) - 1
        parent = int(j / 2)

        while(parent >= 1 and self.heap[parent] < self.heap[j] ):
            self.heap[parent], self.heap[j] = self.heap[j], self.heap[parent]
            j = parent
            parent = int(parent / 2)


    def extractMax():
        pass


    def printHeap(self):
        if self.size == 0:
            return
        parent = 1
        lastParent = (self.size / 2)

        while(parent < lastParent):
                print ("Parent ", self.heap[parent], end = ' ')
                leftChild = 2 * parent

                if leftChild < self.size:
                    print("Left Child ", self.heap[leftChild], end = ' ')
                    rightChild = leftChild + 1
                    if rightChild < self.size:
                        print("Right Child ", self.heap[rightChild], end = ' ')

                parent = parent * 2


                                ### Testcases ###
# heapObj = BinaryHeap()
# heapObj.insert(9)
# heapObj.insert(8)
# heapObj.insert(7)
# heapObj.insert(6)
# heapObj.insert(5)
# heapObj.insert(4)
# heapObj.insert(3)
# heapObj.printHeap()
# heapObj.insert(11)
# heapObj.printHeap()
