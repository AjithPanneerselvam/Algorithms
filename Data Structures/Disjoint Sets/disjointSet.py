"""
Disjoint-set Data Structure

Time Complexity:
    Union - O(log n)
    Find Root - O(log n)
Space Complexity - O(n)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.rank = 1


class DisjointSet:
    def __init__(self):
        self.DSet = {}


    def makeSet(self, val):
        node = Node(val)
        node.parent = node
        self.DSet[val] = node


    def connected(self, a, b):
        """ are 'a' and 'b' in the same component? """
        if self.findRoot(a) == self.findRoot(b):
            return True
        else:
            return False


    def union(self, a, b):
        rootA = self.findRoot(a)
        rootB = self.findRoot(b)

        if rootA == rootB:
            return
        elif rootA.rank >= rootB.rank:
            if rootA.rank == rootB.rank:
                rootA.rank += 1
            rootB.parent = rootA
        else:
            rootA.parent = rootB


    def findRoot(self, data):
        temp = self.DSet[data]
        while(temp != temp.parent):
            temp = temp.parent
        return temp


    def count(self):
        """ Returns the number of Disjoint-Sets """
        numDSets = 0
        for val in self.DSet:
            if self.DSet[val] != val:
                numDSets += 1
        return numDSets



#                               ### Testcases ###
# ds = DisjointSet()
# ds.makeSet(1)
# ds.makeSet(2)
# ds.makeSet(3)
# ds.makeSet(4)
# ds.makeSet(5)
# ds.makeSet(6)
# ds.makeSet(7)
#
# ds.union(1,2)
# ds.union(2,3)
# ds.union(4,5)
# ds.union(6,7)
# ds.union(5,6)
# ds.union(3,7)
#
#
# for i in range(1,8):
#     rootNode = ds.findRoot(i)
#     print(rootNode.value)
