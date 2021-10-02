class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 0
        c = 0
        while i<len(s):
            ind = i
            while True:
                if ind<len(s) and s[i] == s[ind]:
                    ind+=1
                else:
                    ind-=1
                    break
            c+=sum(cost[i:ind+1])-max(cost[i:ind+1])
            i=ind+1
        return c