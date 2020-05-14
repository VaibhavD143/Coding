import heapq
hp = [2,7,4,1,8,1]
heapq._heapify_max(hp)
def heappush_max(heap,elem):
    heap.append(elem)
    heapq._siftdown_max(heap,0,len(heap)-1)
while len(hp)>1:
    elem = heapq._heappop_max(hp)- heapq._heappop_max(hp)
    if elem:
        heappush_max(hp,elem)
print(hp[0])