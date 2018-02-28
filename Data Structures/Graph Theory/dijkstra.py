"""
Dijkstra Algorithm - Single Source Shortest Path

Time Complexity - O(E log V)
Space Complexity - O(E + V)
"""

import sys
sys.path.insert(0, './../Heap/')
from priorityQueue import PriorityQueue
from undirectedGraph import testcases
# from directedGraph import directedTestcases
INFINITY = sys.maxsize


def dijkstra(graphObj, startVertex):
    pq = PriorityQueue()

    for vertex in graphObj.getVertices():
        if vertex == startVertex:
            pq.insert([0, vertex])
            graphObj.verticesList[startVertex].distance = 0
        else:
            pq.insert([INFINITY, vertex])

    while(len(pq.pqueue)):
        currentVertex = pq.extractMin()

        if len(pq.pqueue) == 1:
            break

        # print(pq.pqueue, pq.lookup)
        for adjNode in graphObj.verticesList[currentVertex[1]].getConnections():
            newDistance = graphObj.verticesList[currentVertex[1]].distance + graphObj.verticesList[currentVertex[1]].adjList[adjNode]
            if newDistance < graphObj.verticesList[adjNode].distance:
                graphObj.verticesList[adjNode].distance = newDistance
                graphObj.verticesList[adjNode].predecessor = currentVertex[1]
                index = pq.lookup[adjNode]
                pq.decreaseKey(index, newDistance)

    return graphObj


def printGraph(graphObj):
    for vertex in graphObj.getVertices():
        print(vertex, graphObj.verticesList[vertex].distance, graphObj.verticesList[vertex].predecessor)


def retrace(graphObj, startVertex, endVertex):
    path = []
    temp = endVertex
    path.append(endVertex)
    while(temp != startVertex):
        temp = graphObj.verticesList[temp].predecessor
        path.append(temp)
    return path[::-1]



#                                           ### Testcases ###
# graphObj = testcases()
# graphObj = dijkstra(graphObj, 'A')
# printGraph(graphObj)
# path = retrace(graphObj, 'A', 'D')
# print(path)
# path = retrace(graphObj, 'A', 'F')
# print(path)
