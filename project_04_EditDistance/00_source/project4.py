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
EditDistance Algorithm

determines the number of edits required to convert one string into another
"""
def ED(src, dest):
    """
    src    # The source/starting string
    dest   # The destination/ending string
    """

    """
    Generation of the dynamic programming table
    note: for the index values, i are the rows and j are the columns
    """
    # the initialization of the dp table.
    dp_table = [[None for i in range(len(dest)+1)] for j in range(len(src)+1)]
    # population of the base cases for row 0.
    for i in range(len(dest)+1):
        dp_table[0][i] = i
    # population of the base cases for column 0.
    for j in range(len(src)+1):
        dp_table[j][0] = j

    # iteratively generate the DP table, starting with the base cases, moving/
    # left to right, top to bottom.
    for i in range(1,len(src)+1):
        for j in range(1,len(dest)+1):
            # [left/insert, down/delete, diagonal/sub_or_match]
            three_ops = [dp_table[i][j-1],dp_table[i-1][j],dp_table[i-1][j-1]]
            edit_cost = min(three_ops)

            # if match: do not update edit cost, else: update edit cost.
            if src[i-1] == dest[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
            else:
                dp_table[i][j] = 1 + edit_cost

    """
    # code chunk to look at DP Table
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in dp_table]))
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in edit_table]))
    """

    """
    Using the dpTable to trace back the optimal edit operations
    """
    # initialize index values at the bottom right of DP table.
    i = len(src)
    j = len(dest)

    # initialize edits list to record what edits were made.
    edits = []
    op_names = ['insert','delete','sub','match']

    # general base case.
    while i!=0 and j!=0:
        # b/c there two diagonal values, determine if the diagonal value is/
        # match or substitute. if values are the same: match, else: use DP/
        # table to determine operation.
        # Match:
        if src[i-1] == dest[j-1]:
            i-=1
            j-=1
            edits.append(('match',src[i],i))
        else:
            #evaluate which values from the dp_table gives the optimal value.
            three_ops = [dp_table[i][j-1],dp_table[i-1][j],dp_table[i-1][j-1]]
            edit_cost = min(three_ops)
            edit_index = three_ops.index(edit_cost)
            # Insert:
            if edit_index == 0:
                j-= 1
                edits.append((op_names[edit_index],dest[j],i))
            # Delete:
            elif edit_index == 1:
                i-=1
                edits.append((op_names[edit_index],src[i],i))
            # Substitute:
            else:
                i-=1
                j-=1
                edits.append((op_names[edit_index],dest[j],i))

    # edge case: when in leftmost column, i.e. j = 0.
    while i!=0:
        i-=1
        edits.append(('delete',src[i],i))

    # edge case: when in top row, i.e. i = 0.
    while j!=0:
        j-=1
        edits.append(('insert',dest[j],i))

    # the total edits made/distance traveled.
    dist=dp_table[-1][-1]
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
