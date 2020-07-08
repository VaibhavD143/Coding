from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s)<2:
            return s
        cnt = Counter(s)
        #impossible when length is greater than 1 and only 1 alphabet
        if len(cnt)<2:
            return ""
        
        keys = sorted(cnt,key=lambda k:cnt[k],reverse=True)
        
        #any character occuring more than n//2 times then not possible, that extra shit is to handl odd length
        if cnt[keys[0]]>(len(s)//2+(len(s)&1)):
            return ""
        #solution is possible, so generate string
        res = [keys[0]]*cnt[keys[0]]
        ind = 0
        for k in keys[1:]:
            for _ in range(cnt[k]):
                res[ind]+=k
                ind=(ind+1)%len(res)
        return ''.join(res)