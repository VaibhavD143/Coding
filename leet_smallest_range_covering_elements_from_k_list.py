import heapq

lst = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30],[1]]
lst = [[1]]
ilst = [0]*len(lst)
minHeap = []
maxHeap = lst[0][0]

for i in range(len(lst)):
    heapq.heappush(minHeap,[lst[i][0],i])
    maxHeap = max(maxHeap,lst[i][0])

rangeLen = float('inf')
rangeL = rangeH = None

while True:
    print(minHeap)

    val,ind = heapq.heappop(minHeap)
    if maxHeap-val < rangeLen:
        rangeL = val
        rangeH = maxHeap
        rangeLen = rangeH-rangeL
    newInd = ilst[ind] = 1+ilst[ind]
    if newInd >= len(lst[ind]):
        break
    maxHeap = max(maxHeap,lst[ind][newInd])
    heapq.heappush(minHeap,[lst[ind][newInd],ind])

print(rangeL,rangeH)


