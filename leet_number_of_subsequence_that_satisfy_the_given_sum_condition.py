"""
Intution:
make pair (x,y) in sorted array such that sum of them will be lesser than target and every elements fall between them can be part of subsequence. So 2**diff
diff : # of elements between x and y
as x is max number such that x+y is lesser than target, all lesse than x can also form subsequence. so (2**ind)-1, because with each additional element it multiplies with 2
take example and understand
can be done using window
"""
import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        pw = [1,2]
        def getPow(n):
            if len(pw)<n+1:
                while len(pw)<n+1:
                    pw.append((pw[-1]*2)%MOD)
            return pw[n]
        MOD = 10**9+7
        nums.sort()
        cnt=0
        for i,n in enumerate(nums):
            if n*2 <= target:
                cnt+=getPow(i)
                cnt%=MOD
            elif n<target:
                ind = bisect.bisect(nums,target-n)
                if ind == 0:
                    continue
                diff = i-ind
                cnt+= (getPow(diff))*(getPow(ind)-1)
                cnt%=MOD
            else:
                break
        return cnt