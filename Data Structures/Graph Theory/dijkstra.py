"""
Dijkstra Algorithm - Single Source Shortest Path
"""

import sys
sys.path.insert(0, './../Heap/')
from priorityQueue import PriorityQueue
from undirectedGraph import undirectedTestcases
# from directedGraph import directedTestcases
INFINITY = sys.maxsize


def dijkstra(graphObj, startVertex):
    pq = PriorityQueue()
    for vertex in graphObj.getVertices():
        if vertex == startVertex:
            pq.insert([0, vertex])
        else:
            pq.insert([INFINITY, vertex])

    graphObj.verticesList[startVertex].distance = 0

    while(len(pq.pqueue)):
        currentVertex = pq.extractMin()
        if len(pq.pqueue) == 1:
            break

        for adjNode in graphObj.verticesList[currentVertex[1]].getConnections():
            newDistance = graphObj.verticesList[currentVertex[1]].distance + graphObj.verticesList[currentVertex[1]].adjList[adjNode]
            if newDistance < graphObj.verticesList[adjNode].distance:
                oldDistance = graphObj.verticesList[adjNode].distance
                graphObj.verticesList[adjNode].distance = newDistance
                graphObj.verticesList[adjNode].predecessor = currentVertex[1]
                index = pq.pqueue.index([oldDistance, adjNode])
                pq.decreaseKey(index, newDistance)
                graphObj.verticesList[adjNode].predecessor = currentVertex[1]

    for vertex in graphObj.getVertices():
        print(vertex, graphObj.verticesList[vertex].distance, graphObj.verticesList[vertex].predecessor)
    return graphObj


def retrace(graphObj, startVertex, endVertex):
    path = []
    temp = endVertex
    path.append(endVertex)
    while(temp != startVertex):
        temp = graphObj.verticesList[temp].predecessor
        path.append(temp)
    return path[::-1]



#                                           ### Testcases ###
# graphObj = undirectedTestcases()
# graphObj = dijkstra(graphObj, 'u')
# path = retrace(graphObj, 'u', 'w')
# print(path)
# path = retrace(graphObj, 'u', 'z')
# print(path)
