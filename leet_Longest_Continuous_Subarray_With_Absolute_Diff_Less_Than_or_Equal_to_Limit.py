from collections import deque
lst = [10,1,2,4,7,2]
# lst = [4,2,2,2,4,4,2,2]
# lst = [3,2,2,1,3]
lst = [7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87]
# lst = [49, 26, 45, 13, 27, 74, 87, 56, 76, 25, 64]
# lst= [7,40,10,10,40]
limit = 63
# limit = 5
l,r,mind,maxd = 0,0,0,0
minq,maxq = deque([]),deque([])
res =0
print(lst)
for r in range(len(lst)):
    print(l,r,mind,maxd,minq,maxq,lst[r])
    #minCase
    if lst[r]<=lst[mind]:
        mind = r
        # minq.clear()
    #maxCase
    if lst[r]>= lst[maxd]:
        maxd=r
        # maxq.clear()
    while maxq and lst[maxq[-1]]<=lst[r]:
        maxq.pop()
    maxq.append(r)
    while minq and lst[minq[-1]]>=lst[r]:
        minq.pop()
    minq.append(r)
    if lst[maxd]-lst[mind] <= limit:
        res = max(res,r-l+1)
        print("Result : ",res,lst[maxd],lst[mind],lst[maxd]-lst[mind])
    else:
        #max was changed then move l index with minq
        if lst[r] == lst[maxd]:
            l=1+mind
            mind = minq.popleft()
            while lst[maxd]-lst[mind] > limit:
                l=mind+1
                mind = minq.popleft()
        else:
            l=1+maxd
            maxd = maxq.popleft()
            while lst[maxd]-lst[mind] > limit:
                l=1+maxd
                maxd = maxq.popleft()
print(res)