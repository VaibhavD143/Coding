"""
Gyaan : the way it is working!!! lit
EX. 1 5 6 2 4 7
subs:
1
1 5
1 5 6
1 2 6
1 2 4
1 2 4 7
"""
import bisect
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        subs=[]
        for num in A:
            ind = bisect.bisect_left(subs,num)
            if not subs or ind == len(subs):
                subs.append(num)
            else:
                subs[ind]=num
        return len(subs)
