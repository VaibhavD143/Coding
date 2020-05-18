"""
Gyaan:
how to unset lowest bit of number!
"""
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        res=0
        while A:
            A = A&(A-1)
            res+=1
        return res