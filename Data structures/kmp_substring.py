"""
Intution:
lps[i]: longest proper prefix and sufix of a string till ith index
str : ABABA
lps : 00123
lps tells us how many character can be skipped while moving patter window in text which makes it O(n)
https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
"""
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, pat, txt):
        if not pat or not txt:
            return -1
        # lps=[0]
        def computeLPS(pat):
            lps=[0]*len(pat)
            length=0    #currently matching prefix suffix len
            i=1         #current index in pattern
            while i<len(pat):
                #if len index from beginning matching then increament length and set it as lps
                if pat[i]==pat[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    #case i.e. AAABAAAAB at 8th index
                    if length !=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        lps = computeLPS(pat)
        i=0
        j=0
        res=[]
        while i<len(txt):
            if pat[j] == txt[i]:
                i+=1
                j+=1
                
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
            if j==len(pat):
                # return i-j
                res.append(i-j)
                j=lps[j-1]
            
        # return -1
        return res