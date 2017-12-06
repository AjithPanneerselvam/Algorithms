"""
Kruskal Algorithm - Minimum Spanning Tree

Time Complexity - O(E log E)
Space Complexity - O(V + E)
"""

from undirectedGraph import Graph
import sys
sys.path.insert(0, './../Disjoint Sets/')
from disjointSet import DisjointSet
import math


def kruskal(edgeWeights, edgeNames):
    minSpanningTree = []
    quicksort(edgeWeights, edgeNames, 0, len(edgeWeights) - 1)
    dsObj = DisjointSet()

    for i in range(len(edgeNames)):
        u = edgeNames[i][0]
        v = edgeNames[i][1]
        if u not in dsObj.DSet:
            dsObj.makeSet(u)
        if v not in dsObj.DSet:
            dsObj.makeSet(v)

        if dsObj.findRoot(u) != dsObj.findRoot(v):
            dsObj.union(u, v)
            minSpanningTree.append((edgeNames[i], edgeWeights[i]))

    return minSpanningTree


def quicksort(edgeWeights, edgeNames, left, right):

    if left < right:
        pivotIndex = partition(edgeWeights, edgeNames, left, right)
        quicksort(edgeWeights, edgeNames, left, pivotIndex - 1)
        quicksort(edgeWeights, edgeNames, pivotIndex + 1, right)
        return edgeWeights


def partition(edgeWeights, edgeNames, left, right):

    ## Choosing first element as the pivot element
    pivotIndex = left
    pivotValue = edgeWeights[pivotIndex]
    i = left

    for j in range(left, right + 1):
        if edgeWeights[j] < pivotValue:
            edgeWeights[i], edgeWeights[j] = edgeWeights[j], edgeWeights[i]
            edgeNames[i], edgeNames[j] = edgeNames[j], edgeNames[i]
            i += 1

    pivotIndex = edgeWeights.index(pivotValue)
    edgeWeights[pivotIndex], edgeWeights[i] = edgeWeights[i], edgeWeights[pivotIndex]
    edgeNames[pivotIndex], edgeNames[i] = edgeNames[i], edgeNames[pivotIndex]

    return i



#                               ### Testcases ###
# g = Graph()
# edgeWeights = [1, 3, 1, 3, 1, 4, 5, 6, 2]
# edgeNames = ['AD', 'AB', 'BC', 'BD', 'CD', 'CF', 'CE', 'DE', 'EF']
#
# for i in range(len(edgeWeights)):
#     g.addEdge(edgeNames[i][0], edgeNames[i][1], edgeWeights[i])
#
# print(kruskal(edgeWeights, edgeNames))
