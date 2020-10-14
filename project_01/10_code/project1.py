"""
Math 560
Project 1
Fall 2020

Partner 1: Sutianyi Wen (sw490)
Partner 2: Joseph Hsieh (jch122)
Date: October 9th, 2020
"""

"""
SelectionSort
"""
import random
def SelectionSort(listToSort):
    # Index of sorted
    length = len(listToSort)
    for i in range (length):
        min_index = i
        # Find the min in the remaining unsorted list
        for j in range(i+1,length):
            if listToSort[j] < listToSort[min_index]:
                min_index = j
                pass
            pass
         # Swapping
        temp = listToSort[i]
        listToSort[i] = listToSort[min_index]
        listToSort[min_index] = temp
        pass
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    length = len(listToSort)
    # The first element is in the sorted part
    for i in range(1,length):
    	# Continuously bubble the ith element to sorted array
        temp = listToSort[i]
        while i-1 >= 0 and temp < listToSort[i-1]:
          listToSort[i] = listToSort[i-1]
          # looks left
          i-=1
        listToSort[i] = temp
    return listToSort
"""
BubbleSort
"""
def BubbleSort(listToSort):
    length = len(listToSort)
    swapped = False
    # Traverse each element
    for i in range (length):
    	# Continuously shrink the window size
        for j in range(length-1-i):
        	# Check if swap is needed
            if listToSort[j] > listToSort[j+1]:
                temp = listToSort[j]
                listToSort[j] = listToSort[j+1]
                listToSort[j+1] = temp
                swapped = True
                pass
            pass
        if not swapped:
           	return listToSort
        pass
    return listToSort
"""
MergeSort
"""
def MergeSort(listToSort):
    length = len(listToSort)
    if length == 1:
        return listToSort
    else:
        split = length//2
        left = MergeSort(listToSort[:split])
        right = MergeSort(listToSort[split:])
        # Allocate array to merge back from left and right
        merged = []
        # Put elements into merge array untill either one is empty
        while left and right:
            num_left,num_right = left[0],right[0]
            if num_left < num_right:
                merged.append(num_left)
                left.pop(0)
                pass
            else:
                merged.append(num_right)
                right.pop(0)
                pass
            pass
        # Put the remaining elements from left/right to merged. Append at the back
        while left:
            merged.append(left[0])
            left.pop(0)
            pass
        while right:
            merged.append(right[0])
            right.pop(0)
            pass
     # Inplace change listToSort
    listToSort[:] = merged[:]
    return listToSort
"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort,i=None,j=None):
    length = len(listToSort)
    if length <= 1:
        return listToSort
    else:
        # randomly pick a pivot and swap it with the last element
        # it's better then directly picking the last index as pivot for sorted input
        pivot_index = random.randint(0,len(listToSort)-1)
        temp = listToSort[pivot_index]
        listToSort[pivot_index] = listToSort[-1]
        listToSort[-1] = temp
        pivot = listToSort[-1]
        # left_ptr and right_ptr moves to meet
        left_index, right_index = 0,len(listToSort)-2
        while True:
        	# While left is smaller than pivot, look left
            while listToSort[left_index] <= pivot and left_index < length -1:
                left_index+=1
                continue
            # Whilte right is larger than pivot, look right
            while listToSort[right_index] >= pivot and right_index > 0:
                right_index-=1
                continue
            # Left meet right, break
            if left_index >= right_index:
                break
            # swap
            else:
                temp = listToSort[left_index]
                listToSort[left_index] = listToSort[right_index]
                listToSort[right_index] = temp
        # Put pivot in the middle
        temp = listToSort[left_index]
        listToSort[left_index] = pivot
        listToSort[-1] = temp
        # Call quicksort on both parts
        listToSort[:]= QuickSort(listToSort[:left_index])+QuickSort(listToSort[left_index:])
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
    measureTime(True)
