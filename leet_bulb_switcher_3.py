class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # lst = []
        # res =0
        # for i in light:
        #     heapq.heappush(lst,-i)
        #     if -lst[0] == len(lst):
        #         res+=1
        # return res
        res=0
        right = 0
        for i,l in enumerate(light):
            right = max(right,l)
            if i+1 ==right:
                res+=1
        return res
        