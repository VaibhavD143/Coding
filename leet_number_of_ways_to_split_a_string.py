"""
Intution:
find length of blocks on both the sides available for partition and then multiply them.
"""
class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9+7
        cnt = s.count('1')
        if cnt%3!=0:
            return 0
        if cnt == 0:
            n = len(s)
            return (((n-1)*(n-2))//2)%MOD
        part = cnt//3
        for i in range(len(s)):
            if s[i]=='1':
                part-=1
            if part == 0:
                ind = i+1
                break
        block1 = 0
        for i in range(ind,len(s)):
            if s[i] == '1':
                break
            block1+=1
        part = cnt//3
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                part-=1
            if part == 0:
                ind = i-1
                break
        block2 = 0
        for i in range(ind,-1,-1):
            if s[i]=='1':
                break
            block2+=1
        return ((block1+1)*(block2+1))%MOD