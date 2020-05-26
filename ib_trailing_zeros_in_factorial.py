class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        cnt = 0
        n=5
        rem=1
        while rem:
            rem = A//n
            cnt+=rem
            n*=5
        return cnt