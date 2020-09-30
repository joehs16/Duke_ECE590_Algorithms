"""
Math 560
Project 1
Fall 2020

Partner 1: Sutianyi (Bill) Wen
Partner 2: Joseph Hsieh
Date:
"""

"""
created a swap function to swap elements in a vector
"""
def swap(input, idx_A, idx_B):
    input[idx_A], input[idx_B] = input[idx_B], input[idx_A]
    return input

x = [1,2,3,4]
swap(x,0,2)
"""
SelectionSort
Step 1: Separate the array into "sorted" and "unsorted" components.
    -> initially, the entire array is "unsorted" and the "sorted" component is
    empty
Step 2: Store the index separating the "sorted" and "unsorted" compnents.
    -> initally, K=0
Step 3: Search the "unsorted" component for the minimum element.
Step 4: Swap this minimum element with the element at index k and increment k

note: This algorithm performs the same regardless of the input,
so there is no difference between best and worst cases.

To fill the kth element of our sorted array, we must ﬁnd the smallest of the
remaining n-k unsorted elements
This happens for every k = 0 ... n-1

Best/Average/Worst Case:
n + (n − 1) + (n − 2) + · · · + 2 + 1 ∈ O(n^2)
"""
def SelectionSort(listToSort):
    for current_idx in range(len(listToSort)):                                  # loop through each value in the list
        k = current_idx                                                         # pointer for the current index of the list
        for idx in range(k+1,len(listToSort)):                                  # this loop compares each unsorted value to the current pointer
            if listToSort[k]>listToSort[idx]:                                   # if the unsorted value is smaller than the current pointer, swap.
                listToSort[k], listToSort[idx] = listToSort[idx], listToSort[k] # swapping indexes
            else:                                                               # if the values are LEQ, then dont do anything
                pass
        pass
    return listToSort

"""
InsertionSort

1. Separate the array into a sorted component and an
unsorted component.
    Originally, the entire array is unsorted, and the sorted component is empty.
2. Store the index separating the sorted and unsorted components starting at the
front of the array.
    So k = 0 originally.
3. Iteratively insert the element at k + 1 into the sorted component.
    - Search backwards (starting at position k) through the sorted component until
we find where the element should go.
    - Shift the remaining sorted elements 1 index to the right.
    - Insert the element in that position.
    - Increment the index k.

Note: this insertion process can also be accomplished with “bubbling”, where we
swap the k + 1 element with the preceding element until it is in the correct location.

"""
def InsertionSort(listToSort):
    for current_idx in range(len(listToSort)-1):
        k = current_idx
        #print(listToSort)
        #print(f"pointer is at idx {k}  (value: {listToSort[k]})")

        if listToSort[k]>listToSort[k+1]:
            #print(f"swap {k} (value: {listToSort[k]}) and {k+1} (value: {listToSort[k+1]})")
            listToSort[k], listToSort[k+1] = listToSort[k+1], listToSort[k] #swapping of values
                #check if new k can move more left
            #for bubble in range(j):
            j = k
            while j>0 and listToSort[j]<listToSort[j-1]:
                #print(f"swap {j} (value: {listToSort[j]}) and {j-1} (value: {listToSort[j-1]})")
                listToSort[j], listToSort[j-1] = listToSort[j-1], listToSort[j] #swapping of values
                j = j-1
            else:                                                               # if the values are LEQ, then dont do anything
                pass
        else:                                                               # if the values are LEQ, then dont do anything
            pass
    return(listToSort)

x = [1,2,4,5,2,6,-4,5,3,1]
InsertionSort(x)

"""
BubbleSort
1. Iterate through the array.
2. Compare every two adjacent elements.
3. If they are out of order, swap them.
4. Repeat until no more swaps are made.

"""
def BubbleSort(listToSort):
    n = 0
    while n<len(listToSort):
        print(f'--loop {n}--')
        x = 0
        while x<(len(listToSort)-1):
            print(f'index: {x}, current list: {listToSort}')
            if listToSort[x]>listToSort[x+1]:
                print(f"> SWAP b/c index {x} and index {x+1} (values: {listToSort[x]} > {listToSort[x+1]})")
                listToSort[x], listToSort[x+1] = listToSort[x+1], listToSort[x]
                print(f'New list: {listToSort}')
                x += 1
            else:
                print(f"> NO SWAP b/c index {x} LEQ index {x+1} (values : {listToSort[x+1]} <= {listToSort[x+1]})")
                x += 1
            pass
        n += 1
    return listToSort

"""
MergeSort

Divide & Conquer Approach
Base Cases:
    - If the array has 1 element, it is sorted.
    - If the array has 2 elements, swap if needed and return.

1. Split the array into two halves.
2. Recursively sort each half.
3. Merge the already sorted halves.
    - Iterate through them simultaneously.
    - Compare their smallest elements.
    - The smaller of the two gets removed and inserted into the
merged array.
    - This merge takes O(n) time when merging two arrays of
size n/2.


"""
def MergeSort(listToSort):
    return listToSort

"""
QuickSort
    - Base Cases: If the array has 1 element, it is sorted.
    - Choose a pivot element.
    - Partition the array based on the pivot. Put everything
smaller than the pivot in front and everything larger than
the pivot in back. O(n)
    - Recurse on each partition.

Note that it is always best to split the array in half because
this minimizes the size of the largest recursive call. This will
depend on our choice of pivot.

How do we choose the pivot?
- Pick the first element in the list. This works very poorly on
already sorted inputs.
- Pick the last element in the list. This also works very poorly
on already sorted inputs.
- Pick a random element in the list.
- Partition based on the median of the first, last, and middle
elements.


Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
