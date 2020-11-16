"""
Math 560
Project 5
Fall 2020

Partner 1:
Partner 2:
Date:
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
    ##### Your implementation goes here. #####
    for ver in adjList:
        ver.cost = math.inf
        ver.prev = None
        ver.visited = False
    # Pick an arbitrary vertex 
    start = adjList[2]
    start.cost = 0
    # Make priority queue
    Q = PriorityQueue(adjList)
    while not Q.isEmpty():
        cur = Q.deleteMin()
        cur.visited=True
        for neighbor in cur.neigh:
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
    ##### Your implementation goes here. #####
    for ver in adjList:
        makeset(ver)
    X = []
    for edge in edgeList:
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
    ##### Your implementation goes here. #####
    v.pi = v
    v.height = 0

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    if v!= v.pi:
        #set our parent to be the root
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
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
    ##### Your implementation goes here. #####
    for ver in adjList:
        ver.visited = False
    tour = []
    stack = []
    tour.append(start.rank)
    stack.append(start)
    while not len(tour)!= 0:
        cur = stack.pop()
        for neighbor in cur.mstN:
            if neighbor.visited==False:
                stack.append(neighbor)
                tour.append(neighbor.rank)
                neighbor.visited=True
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
    print(test_map.mst)
    """
    verb = True # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
