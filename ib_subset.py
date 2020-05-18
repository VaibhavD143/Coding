class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsets(self, A):
        if not A:
            return [[]]
        def addIt(A,ind,lst,res):
            if ind == len(A):
                return
            
            tmp=lst+[A[ind]]
            res.append(tmp)
            addIt(A,ind+1,tmp[:],res)
            addIt(A,ind+1,lst[:],res)
            return
        res=[]
        addIt(sorted(A),0,[],res)
        return [[]]+res
            
            