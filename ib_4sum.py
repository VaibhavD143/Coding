class Solution:
    def fourSum(self, A: List[int], B: int) -> List[List[int]]:
        A.sort()
        res = []
        i=0
        # while i<len(A):
        for i in range(len(A)):
            # j=i+1
            # while j<len(A):
            if i == 0 or A[i]!=A[i-1]:
                for j in range(i+1,len(A)):
                    if j ==i+1 or A[j]!=A[j-1]:
                        l=j+1
                        r=len(A)-1
                        rem = B-A[i]-A[j]
                        while l<r:
                            if A[l]+A[r] == rem:
                                res.append([A[i],A[j],A[l],A[r]])
                                l+=1
                                r-=1
                                while l<r and A[l]==A[l-1]:
                                    l+=1
                                while l<r and A[r] == A[r+1]:
                                    r-=1
                            elif A[l]+A[r]>rem:
                                r-=1
                                # while l<r and A[r]==A[r+1]:
                                #     r-=1
                            else:
                                l+=1
                    # j+=1
                    # while j<len(A) and A[j]==A[j-1]:
                    #     j+=1
            # i+=1
            # while i<len(A) and A[i]==A[i-1]:
            #     i+=1
        return res