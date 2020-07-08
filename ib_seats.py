"""
Intution:
After hitting first 'x', any '.' comes,you are supposed to cross it
so at any point we decide which is cost effienr moving left part 'x' or moving right 'x'
"""
class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        cnt = 0
        l=0
        r=A.count('x')

        for i in A:
            if i == 'x':
                l+=1
                r-=1
            else:
                cnt+=min(l,r)
        return cnt%10000003
