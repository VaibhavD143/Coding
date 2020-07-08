"""
intution :
Sum of digits should be multiple of 3
if already then return
baki smjlo
"""
from collections import Counter
class Solution:
    def largestMultipleOfThree(self, digs: List[int]) -> str:
        cnt = Counter(digs)
        sm = sum(digs)
        def generate(cnt):
            res=""
            for i in range(9,-1,-1):
                res+=str(i)*cnt[i]
            if not res:
                return ""
            return res if res[0]!="0" else "0"
        if sm%3 ==0:
            return generate(cnt)
        if sm%3==1:
            for i in [1,4,7]:
                if cnt[i]:
                    cnt[i]-=1
                    return generate(cnt)
        if sm%3 == 2:
            for i in [2,5,8]:
                if cnt[i]:
                    cnt[i]-=1
                    return generate(cnt)
        if sm%3 == 2:
            c = 2
            for i in [1,4,7]:
                if c and cnt[i]:
                    u= min(cnt[i],c)
                    cnt[i]-=u
                    c-=u
            if c == 0:
                return generate(cnt)
        if sm%3 == 1:
            c = 2
            for i in [2,5,8]:
                if c and cnt[i]:
                    u = min(cnt[i],c)
                    cnt[i]-=u
                    c-=u
        return generate(cnt)