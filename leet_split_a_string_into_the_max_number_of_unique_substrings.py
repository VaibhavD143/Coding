"""
Intution:
simple backtracking
early termination is important i.e. second part of if condition.
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def fun(ind,s,ha):
            nonlocal ans
            if ind == len(s):
                ans = max(ans,len(ha))
                return
                
            tmp = ""
            for i in range(ind,len(s)):
                tmp = s[ind:i+1]
                if tmp not in ha and (len(ha)+(len(s)-i)) >ans:
                    ha.add(tmp)
                    fun(i+1,s,ha)
                    ha.remove(tmp)
            return
        
        ha = set()
        ans=1
        fun(0,s,ha)
        return ans