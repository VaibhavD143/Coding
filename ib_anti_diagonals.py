class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        res=[]
        for i in range(len(A[0])):
            r,c=0,i
            cur=[]
            while r<len(A) and c>=0:
                cur.append(A[r][c])
                r+=1
                c-=1
            res.append(cur)
        for j in range(1,len(A)):
            r,c=j,len(A[0])-1
            cur=[]
            while r<len(A) and c>=0:
                cur.append(A[r][c])
                r+=1
                c-=1
            res.append(cur)
        return res