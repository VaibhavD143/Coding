"""
Intution:
dp[trial][egg] = maxFloors that can be achived with `trial` trails and `egg` eggs
bottom-up will be of O(klogN) as floors are increasing expontetial
dp[trail][egg] = 
we take a 1 move to a floor
if it breaks then we compute dp[trial-1][egg-1]
if it doesn't then we compute dp[trial-1][egg]
"""
class Solution:
    # def __init__(self):
    #     self.ha={}
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        for trial in range(1,len(dp)):
            for egg in range(1,len(dp[0])):
                dp[trial][egg] = dp[trial-1][egg-1]+dp[trial-1][egg]+1
                if dp[trial][egg]>=n:
                    return trial