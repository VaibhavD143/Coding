"""
gyaan :
look at the editorial bc!!
"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if not len(A) or not len(A[0]):
            return 0
        
        if len(A[0])<3:
            return max(A[0][:2]+A[1][:2])
        A[0][0]=A[1][0] = max(A[1][0],A[0][0])
        A[0][1]=A[1][1] = max(A[1][1],A[0][1])
        A[0][2]+=A[1][0]
        A[1][2] = max(A[1][2]+A[1][0],A[0][2])
        for i in range(3,len(A[0])):
            A[0][i] += max(A[1][i-2],A[1][i-3])
            A[1][i] = max(A[1][i]+max(A[1][i-2],A[1][i-3]),A[0][i]) #only one value matters which is max from both, so keeping it here
            
        # for r in A:
        #     print(r)
        return max(A[0][-2:]+A[1][-2:])
#Little modification of complexity
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if not len(A) or not len(A[0]):
            return 0
        
        if len(A[0])<3:
            return max(A[0][:2]+A[1][:2])
        cur_max = max(A[0][:2]+A[1][:2])
        A[1][0] = max(A[1][0],A[0][0])
        A[1][1] = max(A[1][1],A[0][1],A[1][0])
        # A[0][2]+=A[1][0]
        # A[1][2] = max(A[1][2]+A[1][0],A[0][2])
        for i in range(2,len(A[0])):
            tmp = max(A[0][i],A[1][i])
            A[1][i] = max(tmp+A[1][i-2],A[1][i-1])
            
        # for r in A:
        #     print(r)
        return max(A[1][-2:])

#EDITORIAL
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        ''' In each column, there is no point taking
            the lowest number since diagonal adjacency is forbidden.
            So, can simplify the problem and choose a 1D dynamic programming approach.
            
            Then, let m, n be the best solutions obtained so far by respectively picking:
               m: penulitimate element
               n: last element
            At each turn, we can only update m with new value.
            
            Time complexity: O(n),  constant space.
        '''
        
        m, n = 0, 0
        for a, b in zip(*A):
            x = max(a, b)
            # update m (not picking x) and n (picking x)
            m, n = max(m, n), m+x
        return max(m, n)