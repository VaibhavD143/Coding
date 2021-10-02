from collections import Counter
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = Counter([nums1[i]*nums1[j] for i in range(len(nums1)) for j in range(i+1,len(nums1))])
        cnt2 = Counter([nums2[i]*nums2[j] for i in range(len(nums2)) for j in range(i+1,len(nums2))])
        ans = 0
        for n in nums1:
            ans+=cnt2[n*n]
        for n in nums2:
            ans+=cnt1[n*n]
        return ans