import matplotlib.pyplot as plt
import random
import timeit
def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array
def mergeSort(left, right):
    newList = []
    if len(left) == 1 and len(right) == 1:
        if (left[0] < right[0]):
            newList = left + right
        else:
            newList = right + left
    else:
        while len(left) >= 1 and len(right) >= 1:
            if left[0] <= right[0]:
                newList.append(left.pop(0))
            else:
                newList.append(right.pop(0))
        newList = newList + left
        newList = newList + right
    return newList

def merge(list):
    if len(list) == 1:
        return list
    left = list[0:len(list)//2]
    right = list[len(list)//2:]
    leftSorted = merge(left)
    rightSorted = merge(right)
    return mergeSort(leftSorted, rightSorted)
L=[100, 1000, 10000,100000]
dquick= dict()
dmerge=dict()
for x in L:
    lst = (random.sample(range(x + 1), x + 1))
    for _ in range(5):
        start = timeit.default_timer()
        quicksort(lst)
        stop = timeit.default_timer()
        if x in dquick.keys():
            dquick[x] = (stop - start + dquick[x]) / 2
        else:
            dquick[x] = stop - start
        random.shuffle(lst)
        start2 = timeit.default_timer()
        merge(lst)
        stop2 = timeit.default_timer()
        if x in dmerge.keys():
            dmerge[x] = (stop2 - start2 + dmerge[x]) / 2
        else:
            dmerge[x] = stop2 - start2
        random.shuffle(lst)


plt.figure(1)
plt.plot(dmerge.keys(), dmerge.values(), c='b', label='MergeSort')
plt.plot(dquick.keys(), dquick.values(), c='y', label="QuickSort")
plt.title('SORTING ALGORITHMS')
plt.legend()
plt.xlabel("Number of elements")
plt.ylabel("Time of execution(s)")
plt.show()