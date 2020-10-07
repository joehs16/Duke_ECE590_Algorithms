"""
Math 560
Project 1
Fall 2020

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort
"""

def SelectionSort(listToSort):
    # Index of sorted
    length = len(listToSort)
    for i in range (length):
        min_index = i
        for j in range(i+1,length):
            if listToSort[j] < listToSort[min_index]:
                min_index = j
                pass 
            pass
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
    for i in range(1,length):
        while i-1>= 0 and listToSort[i] < listToSort[i-1]:
            temp = listToSort[i]
            listToSort[i] = listToSort[i-1]
            listToSort[i-1] = temp
            i-=1
            pass
        pass
    return listToSort
"""
BubbleSort
"""
def BubbleSort(listToSort):
    length = len(listToSort)
    swapped = False
    for i in range (length):
        j = 0
        for j in range(length-1-j):
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
        #print(left)
        right = MergeSort(listToSort[split:])
        #print(right)
        merged = []
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
        while left:
            merged.append(left[0])
            left.pop(0)
            pass
        while right:
            merged.append(right[0])
            right.pop(0)
            pass
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
        # Last num is the pivot
        pivot = listToSort[-1]
        #print(pivot)
        #Partition
        left_index, right_index = 0,len(listToSort)-2
        while True:
            while listToSort[left_index] <= pivot and left_index < length -1:
                left_index+=1
                continue
            while listToSort[right_index] >= pivot and right_index > 0:
                right_index-=1
                continue
            if left_index >= right_index:
                break
            else:
                temp = listToSort[left_index]
                listToSort[left_index] = listToSort[right_index]
                listToSort[right_index] = temp

        temp = listToSort[left_index]
        listToSort[left_index] = pivot
        listToSort[-1] = temp
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

