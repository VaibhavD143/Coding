"""
Intution:
now to generate a word, each character must have valid previous character in a string before their occurence
- mark all 'c' as valid 'c' as no char before them
- in each loop `curr` is required valid previous character for `nex` char in a string
- map is stored in ha and if all have valid previous character then return res
counting res:
we are supposed to mainain minimum cnt reuired at a time, so first loop is for that

"""
class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        valid = [0]*len(s)
        cnt=0
        res= 0
        for i,val in enumerate(s):
            if val == 'c':
                valid[i]=1
                cnt+=1
            elif val == 'k':
                cnt-=1
            res=max(cnt,res)
        #ex. "croakcroa" it should return -1
        if cnt!=0:
            return -1
        ha = [['c','r'],['r','o'],['o','a'],['a','k']]
        #for a
        for curr,nex in ha:
            ccnt=0
            # ncnt=0
            for j,val in enumerate(s):
                if val == curr:
                    ccnt+=1
                elif val == nex:
                    if ccnt==0:
                        return -1
                    valid[j]=1
                    ccnt-=1
        
        return res