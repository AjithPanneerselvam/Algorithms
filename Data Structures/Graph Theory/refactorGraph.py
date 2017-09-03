"""
Implementation of Graph Data Structure
"""


class Vertex:
    def __init__(self, id):
        self.id = str(id)
        self.adjList = {}

    def addNeighbour(self, nodeId, weight = 0):
        self.adjList[nodeId] = weight

    def getConnections(self):
        return self.adjList.keys()

    def getWeight(self, adjNode):
        return self.adjList[adjNode]

    def getId(self):
        return self.id

    def __str__(self):
        return self.id + " connected to " + str([x.id for x in self.adjList])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertList[id] = newVertex
        return newVertex

    def addEdge(self, fromId, toId, weight = 0):
        if fromId not in vertList:
            startNewVertex = self.addVertex(fromId)
        if toId not in vertList:
            endNewVertex = self.addVertex(toId)
        startNewVertex.addNeighbour(toId, weight)

    def getVertices(self):
        return self.vertList.keys()
