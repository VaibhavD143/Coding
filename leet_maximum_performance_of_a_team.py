"""
Intution:
we will be counting engineer as per the smallest efficiency from team * speed of that engineer. as per the condition
we sort them based on efficiency and iterate of first k workers, as it is almost 'k', so we calculate res with each iteration and don't pop anythnig!
in subsequent engineer, efficiency is going to decrease as we have sorted in reverse
so iff speed of engineer is greater than min speed from Team then only there is a chance of new result.
because if efficiency and speed both decrease then it doesn't make any sense!
"""
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], eff: List[int], k: int) -> int:
        lst = sorted([[x,y] for x,y in zip(speed,eff)],key = lambda i:(i[1],i[0]),reverse=True)
        minspeed = []
        sm = res = 0
        for i in range(k):
            sm+=lst[i][0]
            tres=sm*lst[i][1]
            res = max(res,tres)
            heapq.heappush(minspeed,lst[i][0])
        

        for i in range(k,len(lst)):
            if lst[i][0]>minspeed[0]:
                sm+=lst[i][0]
                sm-=minspeed[0]
                tres = sm*lst[i][1]
                res = max(res,tres)
                heapq.heapreplace(minspeed,lst[i][0])

        return res%1000000007