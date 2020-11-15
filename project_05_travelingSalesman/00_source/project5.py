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
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    X = []
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
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    tour = []
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
