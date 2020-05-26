from collections import deque
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @return a list of integers
	def solve(self, A, B, C, D):
        res = [1]
        # dp=[0]*(max(A,B,C)+1)
        a=0
        b=0
        c=0
        while len(res)<=D:
            res.append(min(A*res[a],B*res[b],C*res[c]))
            if res[-1]==res[a]*A:
                a+=1
            if res[-1]==res[b]*B:
                b+=1
            if res[-1]==res[c]*C:
                c+=1
            
        return res[1:]