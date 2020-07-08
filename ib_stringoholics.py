"""
Intution:
- here at time `t` string `s` will be rotated ((t*(t+1))//2)%len(s) times
- we are supposed to find some time 't' for which rotation is multiple of len(S)
- if string is concatination of small strings then, requires rotations are according to length of substring length
Ex : s = "abcabcabc" will reqire rotation in multiple of 3 and not 9
- to find length of that substring use KMP's lps and find out length of it
- then find `t` for each string and find LCM of them
"""
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        def gcd(a,b):
            if a%b==0:
                return b
            return gcd(b,a%b)
        
        def findLPS(s):
            lps =[0]*len(s)
            length=0
            i=1
            while i<len(s):
                if s[i] == s[length]:
                    length +=1
                    lps[i] = length
                    i+=1
                else:
                    if length!=0:
                        length = lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        
        def findSUB(lps):
            ind =1
            for i in range(len(lps)-1,-1,-1):
                if lps[i]==0:
                    ind=i+1
                    break
            if lps[-1] == len(lps)-ind and lps[-1]%ind==0:
                return ind
            return len(lps)
        
        def findT(s):
            lps = findLPS(s)
            lensub = findSUB(lps)
            t=1
            while True:
                if ((t*(t+1))//2)%lensub == 0:
                    return t
                t+=1
                
        ans = 1
        for s in A:
            t = findT(s)
            ans = (ans*t)//gcd(t,ans)
        return ans%1000000007