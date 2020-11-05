"""
Math 560
Project 4
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
	dest . . .
src
 .
 .
 .
"""
def ED(src, dest):
    dist = 0 # This is a placeholder, remove and implement!
    edits = [] # This is a placeholder, remove and implement!
    op_names = ['insert','delete','sub','match']
    dp_table = [[None for i in range(len(dest)+1)] for j in range(len(src)+1)]
    # initialize base case row 0
    for i in range(len(dest)+1):
        dp_table[0][i] = i
    # intialize base case column 0
    for j in range(len(src)+1):
        dp_table[j][0] = j
    for i in range(1,len(src)+1):
        for j in range(1,len(dest)+1):
            # insert, delete, sub_or_match
            three_ops = [dp_table[i][j-1],dp_table[i-1][j],dp_table[i-1][j-1]]
            edit_cost = min(three_ops)
            edit_index = three_ops.index(edit_cost)
            if src[i-1] == dest[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
            else:
                dp_table[i][j] = 1 + edit_cost
                
    """
    dist = dp_table[-1][-1]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in dp_table]))
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in edit_table]))
    """

    # trace  back from the right bottom cell.
    i = len(src)
    j = len(dest)
    num_insert = 0
    while i!=0 and j!=0:
        if src[i-1] == dest[j-1]:
            edits.append(('match',src[i-1],i-1))
            i-=1
            j-=1
        else:
            three_ops = [dp_table[i][j-1],dp_table[i-1][j],dp_table[i-1][j-1]]
            edit_cost = min(three_ops)
            edit_index = three_ops.index(edit_cost)
            # insert
            if edit_index == 0:
                edits.append((op_names[edit_index],dest[j-1],i))
                j-=1
            # delete
            elif edit_index == 1:
                edits.append((op_names[edit_index],src[i-1],i-1))
                i-=1
            # sub
            else:
                edits.append((op_names[edit_index],dest[j-1],i-1))
                i-=1
                j-=1
    while i!=0:
        edits.append(('delete',src[i-1],i-1))
        i-=1
    while j!=0:
        edits.append(('insert',dest[j-1],i))
        j-=1
    dist=dp_table[-1][-1]
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(True)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
