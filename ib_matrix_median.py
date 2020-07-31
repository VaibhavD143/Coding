class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        if not A or not A[0]:
            return 
        def bs(arr,target):
            lo,hi=0,len(arr)
            while lo<hi:
                mid=lo+(hi-lo)//2
                if arr[mid]<=target:
                    lo=mid+1
                else:
                    hi = mid
            return lo
        lo,hi = 1,10**9
        skip = 1+((len(A)*len(A[0]))//2)
        
        while lo<hi:
            mid = lo+(hi-lo)//2
            cnt=0    
            for r in A:
                cnt+=bs(r,mid)
            # print(mid,cnt,skip)
            if cnt<skip:
                lo=mid+1
            else:
                hi=mid
        return lo

class Solution1:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        def binaryS(lst,target):
            #will return left most index of target if present, if not then index at which it belogns to
            l=0
            r=len(lst)-1
            flag=0
            while l<=r:
                mid = (l+r)//2
                if lst[mid]==target:
                    flag=1
                    break
                elif lst[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            #to get leftmost instance of target
            if flag:
                for i in range(mid-1,-1,-1):
                    if lst[mid]!=lst[i]:
                        break
                    mid-=1
                return mid,1
            #flag is to make sure if elemt exist or not            
            return l,0

        if not A or not A[0]:
            return
        low = 1
        hig = 10**9
        r=len(A)
        c=len(A[0])
        skip=(r*c)//2
        #high-1 , in case of repetation it will stuck in a loop i.e. 1 2 5 5 5 5 7 8 9
        while low<hig-1:
            mid = low+(hig-low)//2
            cnt= 0
            flag =0
            for r in A:
                val,tflag = binaryS(r,mid)
                cnt+=val
                flag = tflag or flag    #flag because it's possible 5 is median but it is not in matrix
            if cnt == skip:
                if flag:
                    return mid
                else:
                    low=mid
            elif cnt<skip:
                low=mid #as it was returing leftmost instance, possible mid is an answer
            else:
                hig=mid-1 #mid can never be an answer
        #when they are out of loop with two possible value, low and hig
        cnt= 0
        flag =0
        for r in A:
            val,tflag = binaryS(r,hig)
            cnt+=val
            flag = tflag or flag
        #if hig is skipping more than required then it should or not part of element not an answer so low
        if cnt > skip or not flag:
            return low
        else:
            return hig