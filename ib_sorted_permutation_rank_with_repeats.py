"""
Intution:
Just the way alogorithm works
- find number permutations from lower characters at that place and skip them
- if repeatation then divide with factorial of it
"""

from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        
        fact=[1]
        for i in range(1,1+len(A)):
            fact.append(fact[-1]*i)
        
        cnt = Counter(A)
        #all unique characters of a string in sorted form
        unique = list(cnt.keys())
        unique.sort()
        rank=0  #result
        rem = len(A)-1  #how many characters are there left, i.e. A= bcaac and we are processing `b` then rem = 4. will help in skipping
        for c in A:
            """
            taking `rem+1` instead of `rem` because we are initially counting `trank` with all the remaining characters.
            i.e bbbaaa and we are processing first `b` then we are taking 6! and then //3! and //3!, we are considering all remaining chars to avoid multiple counitng
            in later part
            """
            trank = fact[rem+1] 
            for val in cnt.values():
                trank//=fact[val]
            #trank now contains number of permutations with rem+1 characters
            #skipping ranks,by putting each character lesser than current character at current position            
            skip=0
            i=0
            while unique[i]!=c:
                rep = cnt[unique[i]]
                #as we have initially consider current character in repeatation, so correcting that,
                skip+=((trank*fact[rep])//fact[rep-1])//(rem+1) #//rem+1 as we have considered fact[rem+1] in place of fact[rem] initially
                i+=1
            rank+=int(skip)
            rank%=1000003
            cnt[c]-=1
            #if no more occurence of character left then remove it
            if cnt[c]==0:
                unique.remove(c)
                del cnt[c]
            rem-=1
        return (rank+1)%1000003
        