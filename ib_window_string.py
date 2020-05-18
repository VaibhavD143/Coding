"""
gyaan:
Dhyan se and dedication se kro bc!
"""
from collections import Counter
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
        cnt = len(B)
        if cnt == 0:
            return ""
        hat = Counter(B)

        l,r=0,0
        resl,resr=None,None
        minLen = float('inf')
        
        while r<len(A):
            if cnt == 0:                
                if A[l] in hat:
                    hat[A[l]]+=1
                    #when character actually makes difference in required characters
                    #i.e. A=BBCD B=BCD, same applies every cnt condition
                    if hat[A[l]]>0:
                        cnt+=1
                l+=1
            else:
                
                if A[r] in hat:
                    if hat[A[r]]>0:
                        cnt-=1
                    hat[A[r]]-=1
                r+=1
                
            if cnt == 0:
                if r-l < minLen:
                    minLen = r-l
                    resl=l
                    resr=r
        #string is right most part, so we try to shrink it from left side if possible
        while l<r:
            
            if A[l] in hat:
                hat[A[l]]+=1
                if hat[A[l]]>0:
                    cnt+=1
                    break
            l+=1
            if cnt == 0:
                if r-l < minLen:
                    minLen = r-l
                    resl=l
                    resr=r
                
        if resl != None:
            return A[resl:resr]
        return ""