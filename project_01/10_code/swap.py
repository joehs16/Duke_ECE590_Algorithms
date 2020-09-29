x = [1, 2, 3, 4, 5]

def swap(input, idx_A, idx_B):
    temp_idx = input[idx_A]
    input[idx_A] = input[idx_B]
    input[idx_B] = temp_idx
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

x = [3,2,2,17,1,3,4,5]
x = [5,4,3,2,1]
SelectionSort(x)

for k in range(len(x)):
    current_idx = k
    for idx in range(current_idx+1,len(x)):
        print(x[current_idx])
        print(x[idx])
        if x[current_idx]>x[idx]:
            x[current_idx], x[idx] = x[idx], x[current_idx]
            #swap(listToSort,listToSort[k],listToSort[idx])
            print("swap")
        elif x[current_idx]==x[idx]:
            pass
        else:
            pass
x
len(x)
for x in
for current_idx in len(x):
    print(current_idx)
for idx in range(4,5):
    print('test')
len(x)
