"""
Intution:
we will be paying worker as per the greates ratio from k workers * quality of that worker. as per the condition
we sort them based on ratio and take first k workers, that is our base res.
in subsequent worker, ratio is going to increase as we have sorted
so iff quality of worker is lesser than max quality from K workers then only there is a chance of new result.
because if ration and quality both increases then it doesn't make any sense!
"""
import heapq
class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], K: int) -> float:
        lst = sorted([[x,y,y/x] for x,y in zip(q,w)],key = lambda i: (i[2],i[1]))
        maxq = []
        sm = res =0
        for i in range(K):
            sm+=lst[i][0]
            heapq.heappush(maxq,-lst[i][0])
        res = sm*lst[K-1][2]
        for i in range(K,len(lst)):
            if -maxq[0]>lst[i][0]:
                sm+=maxq[0] #it is already negative as maxHeap
                sm+=lst[i][0]
                tres = sm*lst[i][2]
                res = min(res,tres)
                heapq.heapreplace(maxq,-lst[i][0])
        return res