x = [1, 2, 3, 4, 5]

def swap(input, idx_A, idx_B):
    input[idx_A], input[idx_B] = input[idx_B], input[idx_A]
    return input





def SelectionSort(listToSort):
    for current_idx in range(len(listToSort)):
        k = current_idx #counter of which index the pointer is on

        for idx in range(k+1,len(listToSort)):
            #print(listToSort[current_idx])
            #print(listToSort[idx])
            if listToSort[k]>listToSort[idx]:
                listToSort[k], listToSort[idx] = listToSort[idx], listToSort[k] #swapping of values
                #print("swap")
            elif listToSort[current_idx]==listToSort[idx]:
                pass
            else:
                pass
    return listToSort

def InsertionSort(listToSort):
        for current_idx in range(len(listToSort)):                                  # loop through each value in the list
            k = current_idx                                                         # pointer for the current index of the list
            for idx in range(k+1,len(listToSort)):                                 # this loop compares each unsorted value to the current pointer
                if listToSort[k]>listToSort[idx]:

    return listToSort

listToSort = [1,3,4,5,2,6]
x[3] > x[4]
swap(x,4,3)
range(len(x))

listToSort = [1,3,4,5,2,6]
for current_idx in range(len(x)):
    k = current_idx
    print(listToSort)
    print(f"pointer is at idx {k}  (value: {listToSort[k]})")
    for idx in range(k+1,len(listToSort)):
            #print(listToSort[current_idx])
            print(f"pointer+ is at idx {idx} (value: {listToSort[idx]})")
            if listToSort[k]>listToSort[idx]:
                print(f"swap {k} (value: {listToSort[k]}) and {idx} (value: {listToSort[idx]})")
                listToSort[k], listToSort[idx] = listToSort[idx], listToSort[k] #swapping of values
                for value in range(k):
                    print("index " +str(k-value))
                    print("left of index "+ str(k-value-1))
            else:
                print("dont swap")

listToSort = [1,2,4,5,2,6,-4,5,3,1]
listToSort = [2,2,2,2,2,2]
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

def BubbleSortOld(listToSort):
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

x = [3,1,5,-4,1,2,4]
BubbleSortOld(x)
BubbleSort(x)

n = len(x)
for idx in range(n):
    print(f'first loop is {idx}')
    for j in range(0, n-idx-1):
        print(f'2nd loop is {j}')



def QuickSort(listToSort, i=0, j=None):
    print(f'list is {listToSort}')
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)-1
    if len(listToSort) <= 1:
        return listToSort
    # Set pivot as end element
    pivot = len(listToSort)-1
    pv = listToSort[pivot] #length minus 1 to account for counting from zero

    print(f'pivot index: [{pivot}], pivot value: {pv}')
    j = pivot-1 #left of pivot
    while i < j:
        # Keep moving lower pointer closer to pivot if values are less than pivot
        print(f'Left pointer is at [{i}]= {listToSort[i]} and Left pointer is at [{j}]= {listToSort[j]}')
        if listToSort[i] < listToSort[j]:
            #print(f'>left pointer is currently at: [{i}], value: {listToSort[i]}')
            #print(f'>right pointer is currently at: [{j}], value: {listToSort[j]}')
            print(f'> No Swap, List remains: {listToSort}')
            i += 1 #if in order, move left pointer up
            j -= 1
            print(f'> Update pointers with no swap, i is [{i}] and j is [{j}]')
        else:
            listToSort[i], listToSort[j] = listToSort[j], listToSort[i]
            print(f'> Swap, Updated list is: {listToSort}')
            i += 1
            j -= 1
            print(f'> Update pointers after swap, i is [{i}] and j is [{j}]')


        # # Keep moving high pointer closer to pivot if values are greater than pivot
        # if listToSort[i] > listToSort[j]:
        #     print(f'left pointer is currently at: [{i}], value: {listToSort[i]}')
        #     print(f'right pointer is currently at: [{j}], value: {listToSort[j]}')
        #     print('swap')
        #     listToSort[i], listToSort[j] = listToSort[j], listToSort[i]
        #     print(f'after swap, list now is {listToSort}')
        #     j -= 1 #if out of order, swap and move right pointer
        #     print('update right pointer, with swap')
        # else:
        #     print('update right pointer, no swap')
        #     j -= 1
    #move right pointer left
    print(f'i is {i} and j is {j}')

    #while i == j and listToSort[i]>listToSort[pv]:
    #    print(f'swap pivots')
    #    listToSort[i], listToSort[pv] = listToSort[], listToSort[i]
    #    print(f'after swap, list now is {listToSort}')
    # Swap pivot
    #listToSort[pivot], listToSort[j-1] = listToSort[j-1], listToSort[pivot]
    # print(listToSort)
    # left = listToSort[:pivot]
    # print(f'left {left}')
    # right = listToSort[pivot+1:]
    # print(f'right {right}')
    # QuickSort(left)
    # QuickSort(right)
    return listToSort

listToSort = [9,1,7,6,1,1,1,2,0]
QuickSort(listToSort)


def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)-1
    if len(listToSort) <= 1:
        return listToSort
    # Set pivot as end element
    pivot = j
    print(pivot)
    pv = listToSort[pivot]
    print(f'pv: {pv}')
    while i < j-1:
        # Keep moving lower pointer closer to pivot if values are less than pivot
        if listToSort[i] <= pv:
            print(f'i {i}')
            i += 1
        # Keep moving high pointer closer to pivot if values are greater than pivot
        if listToSort[j-1] > pv:
            print(f'j-1 {j-1}')
            j -= 1
        if listToSort[i] >= listToSort[j-1]:
            print(listToSort)
            listToSort[i], listToSort[j-1] = listToSort[j-1], listToSort[i]
    # Swap pivot
    listToSort[pivot], listToSort[j-1] = listToSort[j-1], listToSort[pivot]
    print(listToSort)
    left = listToSort[:pivot]
    print(f'left {left}')
    right = listToSort[pivot+1:]
    print(f'right {right}')
    QuickSort(left)
    QuickSort(right)
    return listToSort

listToSort = [1,2,3,4,5,6,7,8,9]
QuickSort(listToSort)
