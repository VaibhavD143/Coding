"""
Intution:
set_sum//length of set  == (average)total sum//total length
so we are converting this problem to constrained subset sum problem with consrtain on legth of subset!
and sum of subset be i*average, where i is number of elements in subset
"""

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        def isPossible(ind,cnt,target):
            #this condition to check ind overflow is not required as we are already cheking len(A)-ind<cnt condition!
            # if ind == len(A):
            #     if cnt ==0 and target ==0:
            #         return True
            #     return False
            #this one is not required as we are putting conditon for cnt == 0
            # if cnt<0:
            #     return False
            if cnt == 0 :
                if target == 0:
                    return True
                return False
            if len(A)-ind<cnt:
                return False

            if (ind,cnt,target) in ha:
                return ha[ind,cnt,target]
            
            ha[ind,cnt,target] = isPossible(ind+1,cnt-1,target-A[ind]) or isPossible(ind+1,cnt,target)
            
            return ha[ind,cnt,target]
        
        ha = {}
        sm = sum(A)
        # avg = sm/len(A)
        #Keeping length of set to n//2 as remaining is covered in other side like 1,8:8,1 ; 2,7:7,2
        for i in range(1,len(A)//2+1):
            #checking if sum is integer then only looking for it
            if i*sm%len(A)==0 and isPossible(0,i,sm*i//len(A)):
                # print(i)
                return True
        return False