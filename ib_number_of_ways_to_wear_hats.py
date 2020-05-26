"""
https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/
"""
from collections import defaultdict
class Solution:
    def numberWays(self, hats):
        ha=defaultdict(list)
        maxHat = 1
        for pers,hatl in enumerate(hats):
            for hat in hatl:
                maxHat = max(maxHat,hat)
                ha[hat].append(pers)
        # print(maxHat)
        # dp[mask][hat] : Number of ways for a given arrangement of assigned person MASK and FROM hat number 'hat'
        # As we are making it valid only when all the person assigned a single unique hat, answer will be in dp[0,1].
        # Stating starting arrangement as `no assigned`(all zeros) and starting hat number `1`
        dp=[[-1]*(maxHat+1) for i in range(2**len(hats))]
        allOne = (1<<len(hats))-1
        def countWays(mask,n):
            nonlocal maxHat
            nonlocal allOne
            
            #if all persons assigned a hat
            if mask == allOne:
                return 1
            #if hat count exceeds maxHat then invalid
            if n>maxHat:
                return 0
            # print(mask,n)
            if dp[mask][n]!=-1:
                return dp[mask][n]
        
            dp[mask][n] = countWays(mask,n+1)%1000000007

            for pers in ha[n]:
                #if pers is already assigned hat in this configuration then skip it
                if mask&(1<<pers) != 0:
                    continue
                dp[mask][n]+=countWays(mask|(1<<pers),n+1)
                dp[mask][n]%=1000000007
            return dp[mask][n]
        # print(ha)
        # print("length:",len(dp),len(dp[0]))
        return countWays(0,1)%1000000007