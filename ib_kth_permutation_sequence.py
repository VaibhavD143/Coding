"""
Intution:
handle case A=1 B=1
otherwise same as dictionary rank
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        if B==1:
            return ''.join(map(str,range(1,A+1)))
        fact = [1]
        for i in range(1,A+1):
            fact.append(fact[-1]*i)
        if B==fact[A]:
            return ''.join(map(str,range(A,0,-1)))
        
        nums = list(range(1,A+1))    
        
        res =""
        i = A-1
        B-=1
        while i:
            rem = B%fact[i]
            skip = B//fact[i]
            res+=str(nums[skip])
            nums.pop(skip)
            if rem == 0:
                break
            B=rem
            i-=1
        
        return res+''.join(map(str,nums))