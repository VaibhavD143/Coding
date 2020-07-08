class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOne(n):
            cnt=0
            while n:
                n=n&(n-1)
                cnt+=1
            return cnt
        arr.sort(key = lambda i :(countOne(i),i))
        return arr