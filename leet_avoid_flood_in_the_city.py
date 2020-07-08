"""
Intution:
https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697703/python-greedy-with-a-heap
"""
import heapq
class Solution:
"""
Intution:
onDay : for a single lake , get all days on which it rains
close: minheap, which stores index of day on which particular lake was full, establishing there is ocurence in future by condition len()>1
"""
    def avoidFlood(self, rains: List[int]) -> List[int]:
        onDay={}
        close = []
        res = [-1 if r>0 else 1 for r in rains]
        for i,lake in enumerate(rains):
            if lake in onDay:
                onDay[lake].append(i)
            else:
                onDay[lake]=deque([i])
        
        for i,r in enumerate(rains):
            
            if r != 0:
                #when we have encountered second occurence of same lake and lake is not dried out yet!
                if i!=onDay[r][0]:
                    return []
                #all previous if any, dried out and after current day, there is occurence
                if len(onDay[r])>1:
                    heapq.heappush(close,onDay[r][1])
            else:
                #if no lake need to dry
                if not close:
                    res[i]=1
                    continue
                #dry the lake, which happen to have closest second occurence of rain
                ind = heapq.heappop(close)
                lake = rains[ind]
                res[i]=lake
                #dried out this lake
                onDay[lake].popleft()
        return res
"""
select zero which is closest to first occurence and as we are doing it while iterating it, closest second occrence will be maintained
"""
    def avoidFlood1(self, rains: List[int]) -> List[int]:
        seen={}
        zeros=[]
        res = [-1 if r>0 else 1 for r in rains]
        for i,r in enumerate(rains):
            if r ==0:
                zeros.append(i)
            elif r in seen:
                ind = bisect.bisect(zeros,seen[r])
                if ind == len(zeros):
                    return []
                res[zeros[ind]] = r
                zeros.pop(ind)
                seen[r]=i
            else:
                seen[r]=i
        return res