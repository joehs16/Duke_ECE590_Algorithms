"""
Math 560
Project 5
Fall 2020

Partner 1: Joe Hsieh, jch122
Partner 2: Sutianyi Wen, sw490
Date: Nov 19, 2020
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    # Initialize all costs to inf and prev to null
    for ver in adjList:
        ver.cost = math.inf
        ver.prev = None
        ver.visited = False
    # Pick an arbitrary vertex and set cost to 0/
    start = adjList[2]
    start.cost = 0
    # Make priority queue using cost for sorting
    Q = PriorityQueue(adjList)
    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it.
        cur = Q.deleteMin()
        cur.visited=True

        # For each edge out of current vertex
        for neighbor in cur.neigh:

            #if the edge leads out, update.
            if not neighbor.visited:
                if neighbor.cost > adjMat[cur.rank][neighbor.rank]:
                    neighbor.cost = adjMat[cur.rank][neighbor.rank]
                    neighbor.prev = cur
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    # Initialize all singleton sets for each vertex
    for ver in adjList:
        makeset(ver)
    # Initialize the empty MST
    X = []

    # Loop through the edges in increasing order
    for edge in edgeList:
        # If the min edge crosses a cut, add it to MST
        u,v = edge.vertices[0],edge.vertices[1]
        if find(u) != find(v):
            X.append(edge)
            union(u,v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    # Create a singleton set containing vertex v
    v.pi = v
    v.height = 0

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    # find which set vertex v belongs to (used for finding cuts)
    if v!= v.pi:
        #set our parent to be the root
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    # merge the sets containing vertices u and v
    ru = find(u)
    rv = find(v)
    if ru == rv:
        return
    # make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # same height
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP
"""

def tsp(adjList, start):
    # reset all vertices to unvisited
    for ver in adjList:
        ver.visited = False

    #initialize list to track path of traveling salesman
    tour = []
    #initalize stack for DFS
    stack = []

    #put root vertex into stack
    stack.append(start)

    while len(stack) != 0:
        #work on current vertex
        cur = stack.pop()

        #condition to work through the stack
        if cur.visited == False:
            #mark vertex as visited
            cur.visited = True

            #add the current vertex to the path of the traveling salesman
            tour.append(cur.rank)

            #consider all of the neighbors of the current vertex and add them/
            #to the stack to determine where the salesman goes to next, i.e. DFS
            #note that although duplicate neighbors will be added to the stack,
            #the while condition will skip over them becuase they will already
            #be marked visited, so using the triangle principles, shortcuts will
            #be generated, returning a tour path of <2*MST
            for neighbor in cur.mstN:
                stack.append(neighbor)

    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    """
    test_map = Map(mapNum=1, MSTalg=kruskal)
    test_map.getMST()
    print(test_map)
    """
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
