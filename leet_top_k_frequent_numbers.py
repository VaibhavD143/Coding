import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cnt = Counter(nums)
        
#         return heapq.nlargest(k,cnt,key = lambda i:cnt[i])
        return [i for i,_ in Counter(nums).most_common(k)]