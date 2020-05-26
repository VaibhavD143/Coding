# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda item:item.start)
        res=[intervals[0]]
        i=1
        while i<len(intervals):
            if res[-1].end>=intervals[i].start:
                res[-1].end=max(res[-1].end,intervals[i].end)
            else:
                res.append(intervals[i])
            i+=1
        return res