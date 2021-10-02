class Solution:
    def stoneGameV(self, arr:List[int]) -> int:
        def rec(lst,left,right,pref):
            if right-left==0:
                return 0
#             if right-left == 1:
#                 return min(lst[left],lst[right])
            
            if dp[left][right]!=-1:
                return dp[left][right]
            res= 0
            for i in range(left+1,right+1):
                l = pref[i]-pref[left]
                r = pref[right+1]-pref[i]
                if l<r:
                    res = max(res,l+rec(lst,left,i-1,pref))
                elif l>r:
                    res = max(res,r+rec(lst,i,right,pref))
                else:
                    res = max(res,l+max(rec(lst,left,i-1,pref),rec(lst,i,right,pref)))
                # print(left,i,right,res)
            dp[left][right] = res
            return res
        
        pref = [0]*(1+len(arr))
        for i in range(1,len(pref)):
            pref[i] = pref[i-1]+arr[i-1]
        dp = [[-1]*len(arr) for _ in range(len(arr))]
        return rec(arr,0,len(arr)-1,pref)              