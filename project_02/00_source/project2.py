"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1:
Partner 2:
Date:
"""
import os
os.getcwd()
os.chdir('../../project_02/00_source')
# os.getcwd()

# Import math and other p2 files.
import math
from p2tests import *


"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""

def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # # load start and exit
    # start_v = maze.start
    # exit_v = maze.exit
    #
    #
    # for vertex in maze.adjList:
    #     #all the vertices initalize as "not visited"
    #     vertex.visted = False
    #     #set previous values to none
    #     vertex.prev = None
    #     #set distances to infinity
    #     vertex.dist = math.inf

    """
    BFS - Breadth First Search
    """
    # Start BFS
    if (alg == 'BFS'):
        #create an empty queue
        frontier = Queue()

        #initialize the distance
        start_v.dist = 0

        #add the starting location to the queue
        frontier.push(start_v.rank)

        while frontier.isEmpty()==False:
            #look at the first vertex in the list
            current = frontier.pop()

            #look at all the neighbors of the current vertex
            for neighbor in maze.adjList[current].neigh:
                #if the vertex hasn't been visited:
                if neighbor.dist==math.inf:
                    #mark as visited
                    neighbor.dist = maze.adjList[current].dist + 1
                    #push the neighbor to the queue
                    frontier.push(neighbor.rank)
                    neighbor.prev = current
                # if neighbor.dist==math.inf:
                #     print(neighbor.rank)
                #     frontier.push(neighbor.rank)
                #     #print(frontier)
                #     neighbor.dist = maze.adjList[current].dist + 1
                #     neighbor.prev = current
                    pass
                pass
            pass
        path = [exit_v]
        while exit_v.prev != None:
            path.insert(0,exit_v.prev)
            #path.append(exit_v.prev)
            exit_v = maze.adjList[exit_v.prev]
            #print(exit_v)
        return path

    """
    DFS - Depth First Search
    This code marks each vertex that is connected to the starting vertex as 'visited'
    """
    # START DFS
    #else:
        #Step 1: Initialize
        #EACH NODE VISITED SET TO FALSE.
        #self.visited = False

        #Step 2: Visit the first room
        #Go to starting room
        #Set Start.visted to True
        #start.visit
        #pushing to stack is visiting the room

        #While the stack is not empty, pop,


    ##### Your implementation goes here. #####

    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
