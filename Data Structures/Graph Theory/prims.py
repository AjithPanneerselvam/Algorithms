"""
Prim's Algorithm - Minimum Spanning Tree

Time Complexity - O(E log V)
Space Complexity - O(E + V)
"""
from undirectedGraph import Graph
import sys
sys.path.insert(0, './../Heap/')
from priorityQueue import PriorityQueue
INFINITY = sys.maxsize


def prims(graphObj, start):
    pq = PriorityQueue()

    for vertex in graphObj.verticesList:
        if vertex == start:
            g.verticesList[vertex].distance = 0
            pq.insert([0, vertex])
            continue
        g.verticesList[vertex].distance = INFINITY
        pq.insert([INFINITY, vertex])

    while(len(pq.pqueue)):
        currentVertex = pq.extractMin()

        if len(pq.pqueue) == 1:
            return

        for adjNode in graphObj.verticesList[currentVertex[1]].getConnections():
            if adjNode in pq.lookup(adjNode):
                newDistance = graphObj.verticesList[currentVertex[1]].getCost(adjNode)
                if newDistance < graphObj.verticesList[adjNode].distance:
                    graphObj.verticesList[adjNode].distance = newDistance
                    graphObj.verticesList[adjNode].predecessor = currentVertex[1]

        return graphObj




#                               ### Testcases ###
g = Graph()
edgeWeights = [1, 3, 1, 3, 1, 4, 5, 6, 2]
edgeNames = ['AD', 'AB', 'BC', 'BD', 'CD', 'CF', 'CE', 'DE', 'EF']

for i in range(len(edgeWeights)):
    g.addEdge(edgeNames[i][0], edgeNames[i][1], edgeWeights[i])
