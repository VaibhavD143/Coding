"""
Gyaan : how to check if nth bit is set or not!
"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        i=1
        res=0
        for _ in range(32):
            res<<=1
            if A&i:
                res+=1
            i<<=1
        return res