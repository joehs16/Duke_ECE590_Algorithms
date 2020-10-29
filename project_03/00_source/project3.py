"""
Math 560
Project 3
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
	for vertex in adjList:
		vertex.dist = math.inf
		vertex.prev = None

	adjList[0].dist = 0
	# |v| - 1 iteration of Bellman-Ford
	for i in range (0,len(adjList)-1):
		for u in adjList:
			for neighbor in u.neigh:
				if neighbor.dist > u.dist + adjMat[u.rank][neighbor.rank] + tol:
					neighbor.dist = u.dist + adjMat[u.rank][neighbor.rank]
					neighbor.prev = u
	dist_1 = [vertex.dist for vertex in adjList]
	# Run for 1 extra iteration, if any values change, there is a negative cost cycle
	
	for u in adjList:
		for neighbor in u.neigh:
			if neighbor.dist > u.dist + adjMat[u.rank][neighbor.rank] + tol:
				neighbor.dist = u.dist + adjMat[u.rank][neighbor.rank]
				neighbor.prev = u

	dist_2 = [vertex.dist for vertex in adjList]
	# No negative cycle
	track = None
	for i in range(len(dist_1)):
		if dist_1[i] == dist_2[i]:
			continue
		else:
			track = adjList[i]
			break
	if track == None:
		return []
	else:
		visited = set()
		cycle = []
		while track.rank not in visited:
			visited.add(track.rank)
			cycle.insert(0,track.rank)
			track = track.prev
		cycle.insert(0,track.rank)
		i = -1
		while cycle[i]!= cycle[0]:
			cycle.pop(i)
		print(cycle)
		return cycle
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
    #c = Currencies(0)
    #print(c.adjList)
    #print(c.adjMat)
    #cycle = detectArbitrage(c.adjList,c.adjMat)
    #sprint(cycle)
