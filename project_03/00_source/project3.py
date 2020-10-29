"""
Math 560
Project 3
Fall 2020

Partner 1: Sutianyi Wen
Partner 2: Joseph Hsieh
<<<<<<< Updated upstream
Date: 10/29/20
=======
Date: Date: 10/29/20
>>>>>>> Stashed changes
"""

# Import math and p3tests.
import math
from p3tests import *

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
	#initialize the distances for each vertex
	for vertex in adjList:
		vertex.dist = math.inf
		vertex.prev = None

	adjList[0].dist = 0
	# |v| - 1 iteration of Bellman-Ford
	for i in range (0,len(adjList)-1):
		for u in adjList:

			#updating distances if a shorter distance is found. Tol accounts
			#for rounding in normal aribtrage value compared to python float
			for neighbor in u.neigh:
				if neighbor.dist > u.dist + adjMat[u.rank][neighbor.rank] + tol:
					neighbor.dist = u.dist + adjMat[u.rank][neighbor.rank]
					neighbor.prev = u
	#create an instance of graph after Bellman-Ford Alg
	dist_1 = [vertex.dist for vertex in adjList]

	# Run for 1 extra iteration, if any values change, there is a negative /
	# cost cycle
	for u in adjList:
		for neighbor in u.neigh:
			if neighbor.dist > u.dist + adjMat[u.rank][neighbor.rank] + tol:
				neighbor.dist = u.dist + adjMat[u.rank][neighbor.rank]
				neighbor.prev = u

	#create an instance of graph after one more interation of Bellman-Ford
	dist_2 = [vertex.dist for vertex in adjList]

	# initialize a tracking variable to identify vertices that are within/
	# the negative cost cycle, i.e. currencies that are part of the aribtrage
	track = None

	# compare graphs, recording the vertices that changed
	for i in range(len(dist_1)):
		if dist_1[i] == dist_2[i]:
			continue
		else:
			track = adjList[i]
			break

	# account for case of no aribtrage
	if track == None:
		return []

	# account of the removal of vertices that were captured by track/
	# marker but are not actually part of the negative cost cycle

	else:
		#visited = []
		cycle = []

		while track.rank not in cycle: ##modified to remove visited, because i think it was redundant
			#visited.insert(0,track.rank)
			##print("visited: ",visited)
			cycle.insert(0,track.rank)
			##print("cycle: ", cycle)
			track = track.prev
		cycle.insert(0,track.rank)
		i = -1
		#removal of the upstream vertices not in the negative cost cycle
		while cycle[i]!= cycle[0]:
			cycle.pop(i)
		print(cycle)
		return cycle

"""
rates2mat
"""
def rates2mat(rates):
    # returns -log of the currency rate so Bellman-Ford can be implemented
    return [[-math.log(R) for R in row] for row in rates]

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