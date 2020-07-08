class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A.sort()
        min_diff = float('inf')
        for i in range(len(A)):
            l=i+1
            r=len(A)-1
            rem = B-A[i]
            while l<r:
                if abs(rem-A[l]-A[r])<min_diff:
                    res =A[i]+A[l]+A[r]
                    min_diff = abs(rem-A[l]-A[r])
                if A[l]+A[r]>rem:
                    r-=1
                else:
                    l+=1
        return res
            