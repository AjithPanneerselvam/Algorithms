"""
Implementation of Undirected Graph
"""

class Vertex:
    def __init__(self, label):
        self.label = str(label)
        self.adjList = {}
        self.color = None
        self.distance = 0
        self.predecessor = None

    def addNeighbour(self, toVertex, cost = 0):
        self.adjList[toVertex] = cost

    def getConnections(self):
        return self.adjList.keys()

    def getLabel(self):
        return self.label

    def getCost(self, toVertex):
        return self.adjList[toVertex]

    def setColor(self, colorValue):
        self.color = colorValue

    def getColor(self):
        return self.color

    def __str__(self):
        return self.label + " connected to " + str([x for x in self.adjList])


class Graph:
    def __init__(self):
        self.verticesList = {}
        self.numVertices = 0

    def addVertex(self, label):
        self.numVertices += 1
        newVertex = Vertex(label)
        self.verticesList[label] = newVertex
        return newVertex

    def addEdge(self, firstVertex, secondVertex, cost = 0):
        if firstVertex not in self.verticesList:
            firstNewVertex = self.addVertex(firstVertex)
        if secondVertex not in self.verticesList:
            secondNewVertex = self.addVertex(secondVertex)
        self.verticesList[firstVertex].addNeighbour(secondVertex, cost)
        self.verticesList[secondVertex].addNeighbour(firstVertex, cost)

    def getVertices(self):
        return self.verticesList.keys()

    def verticesCount(self):
        return self.numVertices

    def displayGraph(self):
        for vertex in self.verticesList:
            print (self.verticesList[vertex])



# Testcase - Undirected graph
def undirectedTestcases():
    g = Graph()

    for i in range(6):
        g.addVertex(chr(ord('u') + i))

    g.addEdge('u','v',2)
    g.addEdge('u','x',1)
    g.addEdge('u','w',5)
    g.addEdge('v','w',3)
    g.addEdge('v','x',2)
    g.addEdge('x','w',3)
    g.addEdge('x','y',1)
    g.addEdge('w','y',1)
    g.addEdge('w','z',5)
    g.addEdge('y','z',1)


    # print (g.getVertices())
    # print (g.verticesCount())
    # g.displayGraph()

    return g
