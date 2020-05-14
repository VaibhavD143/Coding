# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new):
        i=0
        res=[]
        while i<len(intervals) and new.start>intervals[i].end:
            res.append(intervals[i])
            i+=1
        # when it is skipping all of them
        if i ==len(intervals):
            return res+[new]
        # merge.end = new.end //when it only falls into single current interval
        merge = Interval(min(intervals[i].start,new.start),new.end)
        while i<len(intervals) and new.end>=intervals[i].start:
            merge.end = max(intervals[i].end,merge.end) #if falls into interval then update it
            i+=1
        res+=[merge]+intervals[i:]
        return res
        
        