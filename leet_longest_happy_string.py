import heapq
a = 1
b = 1
c = 7
lst = []
if a:
    heapq.heappush(lst,[-a,'a'])
if b:
    heapq.heappush(lst,[-b,'b'])
if c:
    heapq.heappush(lst,[-c,'c'])

res = ""
while lst:
    elem1,char1 = heapq.heappop(lst)
    if len(res)>=2 and res[-1]==res[-2]==char1:
        if not lst:
            print(res)
            exit(1)
        elem2,char2 = heapq.heapreplace(lst,[elem1,char1])
        res+=char2
        elem2+=1
        if elem2:
            heapq.heappush(lst,[elem2,char2])
    else:
        res+=char1
        elem1+=1
        if elem1:
            heapq.heappush(lst,[elem1,char1])
print(res)