class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        mx = len(s)
        mn = 0
        for i,val in cnt.items():
            mn+=val&2
            
        return mn<=k<=mx