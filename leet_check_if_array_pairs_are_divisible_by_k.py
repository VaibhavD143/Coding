"""
Intution:
Can be done using counter easily
"""
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        for i in range(len(arr)):
            arr[i] = arr[i]%k
        arr.sort()
        i=0
        cnt=0
        while i<len(arr) and arr[i] == 0:
            cnt+=1
            i+=1
        if cnt&1:
            return False
        l,r=i,len(arr)-1
        while l<r:
            if arr[l]+arr[r] != k:
                return False
            l+=1
            r-=1
        return True