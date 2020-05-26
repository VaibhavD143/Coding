class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        l,r=0,0
        ll,lr=0,0
        curr,glb=0,0
        while r<len(A):
            if A[r]=='0':
                curr+=1
                r+=1
            else:
                curr-=1
                r+=1
            if curr>glb:
                glb=curr
                ll=l
                lr=r
            elif curr<0:
                l=r
                curr=0
        return [ll+1,lr] if ll!=lr else []