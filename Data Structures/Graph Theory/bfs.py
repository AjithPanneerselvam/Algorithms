"""
Breadth First Search
Time-Complexity - O(V + E)
Space-Complexity - O(V)
"""

from undirectedGraph import testcases
from collections import deque


def bfs(startVertex):
    g = testcases()
    queue = deque()

    for vertex in g.verticesList:
        g.verticesList[vertex].setColor('white')

    g.verticesList[startVertex].setColor('grey')
    queue.append(g.verticesList[startVertex])

    while(len(queue)):
        poppedVertex = queue.popleft()

        for adjVertex in poppedVertex.adjList:
            if g.verticesList[adjVertex].getColor() == 'white':
                g.verticesList[adjVertex].setColor('grey')
                queue.append(g.verticesList[adjVertex])

        poppedVertex.setColor('black')
        print (poppedVertex.getLabel())


                                    ### Testcases ###
# bfs('u')
