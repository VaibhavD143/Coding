"""
Intution:
set_sum//length of set  == (average)total sum//total length
so we are converting this problem to constrained subset sum problem with consrtain on legth of subset!
and sum of subset be i*average, where i is number of elements in subset

"""
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        def findSubsetSum(ind,cnt,target):
            if cnt ==0:
                if target == 0:
                    return True
                return False
            
            if len(A)-ind<cnt:
                return False
            
            if (ind,cnt,target) in ha:
                return False
            
            path.append(ind)
            if findSubsetSum(ind+1,cnt-1,target-A[ind]):
                return True
            path.pop()
            
            if findSubsetSum(ind+1,cnt,target):
                return True
            ha.add((ind,cnt,target))
            return False
        A.sort()
        ha=set()
        sm = sum(A)
        path=[]
        for i in range(1,len(A)//2+1):
            if i*sm%len(A) ==0 and findSubsetSum(0,i,i*sm//len(A)):
                # print(path)
                res1=[]
                res2=[]
                ind=0
                for j in range(len(A)):
                    if ind<len(path) and j == path[ind]:
                        res1.append(A[j])
                        ind+=1
                    else:
                        res2.append(A[j])
                return [res1,res2]
        return []
        