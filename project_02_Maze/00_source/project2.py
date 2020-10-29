"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1:
Partner 2:
Date:
"""

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
    # load start and exit
    start_v = maze.start
    exit_v = maze.exit
    # Start BFS
    if(alg == 'BFS'):
        frontier = Queue()
    if(alg == 'DFS'):
        frontier = Stack()
    start_v.dist = 0
    frontier.push(start_v.rank)
    while frontier.isEmpty()==False:
        current = frontier.pop()
        for neighbor in maze.adjList[current].neigh:
            if neighbor.dist==math.inf:
                frontier.push(neighbor.rank)
                neighbor.dist = maze.adjList[current].dist + 1
                neighbor.prev = current
                pass
            pass
        pass
    path = [exit_v.rank]
    while exit_v.prev != None:
        path.insert(0,exit_v.prev)
        exit_v = maze.adjList[exit_v.prev]
    return path



"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)
