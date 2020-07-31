"""
Intution:
     2   4   6
   +------------
 1 | _3   5   7
 7 |  9  11  13
11 | 13  15  17
we start from 1,2 and then we expose two other possible answer that is one on right and one below it!
"""
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        ha = [(nums1[0]+nums2[0],0,0)]
        res = []
        seen = set([(0,0)])
        while ha and len(res)<k:
            _,i,j = heapq.heappop(ha)
            res.append((nums1[i],nums2[j]))
            if i+1<len(nums1) and (i+1,j) not in seen:
                heapq.heappush(ha,(nums1[i+1]+nums2[j],i+1,j))
                seen.add((i+1,j))
            if j+1<len(nums2) and (i,j+1) not in seen:
                heapq.heappush(ha,(nums1[i]+nums2[j+1],i,j+1))
                seen.add((i,j+1))
        return res