# num = "1432219"
num = "34012219"
num = "10200"
num = "12"
k=2
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ss = [-1]   #so no need to do an extra check when there is '0'
        for i,val in enumerate(num):
            while len(ss)>1 and k and ss[-1]>val:
                ss.pop()
                k-=1
            if k==0:
                return str(int((''.join(ss[1:]))+num[i:]))
            ss.append(val)
        
        return str(int(''.join(ss[1:len(ss)-k] if ss[1:len(ss)-k] else ["0"]))) #str(int()) to remove leading zeros in case 00222