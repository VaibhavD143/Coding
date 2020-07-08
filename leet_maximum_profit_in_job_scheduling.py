"""
Intution:
To keep track of maximum profit based on endtime
we are sorting based on endTime
[s+1] : because we are storing [endTime,profit] in dp, so [5]<[5,4] to avoid this, as we are using bisect.bisect_right()
"""
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        mem = sorted(zip(endTime,startTime,profit))
        # ha = {1:0}
        # lst = [1]
        # # print(mem)
        # for e,s,p in mem:
        #     pre = bisect.bisect(lst,s)-1
        #     np = p+ha[lst[pre]]
        #     end = bisect.bisect(lst,e)-1
        #     if np>ha[lst[end]]:
        #         ha[e] = np
        #         bisect.insort(lst,e)
        # return max(ha.values())
        dp = [[1,0]]
        for e,s,p in mem:
            ind = bisect.bisect(dp,[s+1])-1
            if dp[ind][1]+p>dp[-1][1]:
                dp.append([e,dp[ind][1]+p])
            # print(dp,ind)
        return dp[-1][1]            
            