import heapq
import random
import timeit
import matplotlib.pyplot as plt

BinHeapDelMax=dict()
BinHeapGetMax=dict()
BinHeapRandInse=dict()
L=[10 ,100, 1000, 10000, 100000]
H=[]
for x in L:
    for k in range(1,10):
        lst = (random.sample(range(x + 1), x + 1))
        for ele in lst[1:]:
            heapq.heappush(H, ele)
        heapq._heapify_max(lst)
        a=lst[0]
        start = timeit.default_timer()
        heapq.heappush(H,a)
        stop = timeit.default_timer()
        if x in BinHeapRandInse.keys():
            BinHeapRandInse[x] = (stop - start + BinHeapRandInse[x])/2
        else:
            BinHeapRandInse[x]= stop-start

        start1 = timeit.default_timer()
        H[0]
        stop1 = timeit.default_timer()

        if x in BinHeapGetMax.keys():
            BinHeapGetMax[x] = (stop1 - start1 + BinHeapGetMax[x])/2
        else:
            BinHeapGetMax[x]= stop1-start1

        c = H[0]
        start2=timeit.default_timer()
        heapq._heappop_max(H)
        stop2=timeit.default_timer()
        heapq.heappush(H, c)
        if x in BinHeapDelMax.keys():
            BinHeapDelMax[x] = (stop2 - start2 + BinHeapDelMax[x]) / 2
        else:
            BinHeapDelMax[x] = stop2 - start2

plt.figure(1)
plt.plot(BinHeapRandInse.keys(), BinHeapRandInse.values(), c='b',  label='Random Insertion')
plt.plot(BinHeapGetMax.keys(), BinHeapGetMax.values(), c='black', label='Get Max')
plt.plot(BinHeapDelMax.keys(), BinHeapDelMax.values(), c='r', label='Del Max')
plt.legend()
plt.show()