class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        cnt=0
        swap = 0
        for i in A:
            if swap:
                i=1-i
            if not i:
                cnt+=1
                swap=1-swap
        return cnt