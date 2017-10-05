"""
Breadth First Search - Directed Graph

Time Complexity - O(V + E)
Space Complexity - O(V)
"""
from directedGraph import testcases
from collections import deque


def bfs(graphObj, startVertex):
    queue = deque()

    graphObj.verticesList[startVertex].setColor("grey")
    queue.append(graphObj.verticesList[startVertex])

    while(len(queue)):
        poppedVertex = queue.popleft()

        for adjVertex in graphObj.verticesList[poppedVertex.getLabel()].getConnections():
            if(graphObj.verticesList[adjVertex].getColor() == "white"):
                queue.append(graphObj.verticesList[adjVertex])
                graphObj.verticesList[adjVertex].setColor("grey")

        graphObj.verticesList[poppedVertex.getLabel()].setColor("black")
        print(poppedVertex.getLabel())


#                                   ### Testcases ###
graphObj = testcases()
bfs(graphObj, 'A')
