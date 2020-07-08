"""
Intution : 
It is same as house robber II but with some modification!
from given array of size 3n elements choose n elements with max sum
no two elements are adjacent to each other!
so we divide it into two problems as we can't select 1st and last element in one go(circular list):
1) ignore last element
2) ignore first element
dp1[k][i] : stores maximum sum possible from selecting k elements till (i-1)th index
dp2[k][i] : stores maximum sum possible from selecting k elements till (i)th index
"""
class Solution:
    def maxSizeSlices(self, w: List[int]) -> int:
        k = len(w)//3
        
        #last element is excluded
        dp1 = [[0]*(len(w)) for _ in range(k+1)]
        #first element is excluded
        dp2 = [[0]*(len(w)) for _ in range(k+1)]
        
        for n in range(1,k+1):
            for i in range(1,len(w)):
                
                if i==1:
                    dp1[n][i] = w[i-1]
                    dp2[n][i] = w[i]
                    continue
                
                dp1[n][i] = max(dp1[n-1][i-2]+w[i-1],dp1[n][i-1])
                dp2[n][i] = max(dp2[n-1][i-2]+w[i],dp2[n][i-1])
        # # print("dp1")
        # for r in dp1:
        #     print(r)
        # # print("dp2")
        # for r in dp2:
        #     print(r)
        return max(dp1[-1][-1],dp2[-1][-1])
                    
                    