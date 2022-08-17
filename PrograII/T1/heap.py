import heapq
from heapq import *

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

print("Head value of heap : ", (heapq.nsmallest(1, heap)))

print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
print("\n")
  
element = heappop(heap)
print(str(element)+"\n")

print("The heap elements : ")
for i in heap:
    print(i, end = ' ')