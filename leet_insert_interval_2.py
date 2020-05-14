intervals = [[3,5],[6,7],[8,10],[13,16]]
newInterval = [9,15]
newInterval = [9,11]
newInterval = [11,15]
newInterval = [17,19]
newInterval = [15,19]
newInterval = [1,2]
newInterval = [1,4]
newInterval = [11,11]
# intervals = []
# newInterval = [4,8]

ind = 0
left = 0
right = len(intervals)-1

while left<len(intervals) and intervals[left][1] < newInterval[0]:
    left+=1

while right >= 0 and intervals[right][0] > newInterval[1]:
    right-=1
# s,e = newInterval[0],newInterval[1]
if left <= right:
    newInterval[0] = min(newInterval[0],intervals[left][0])
    newInterval[1] = max(newInterval[1],intervals[right][1])
print(intervals[:left]+[newInterval]+intervals[right+1:])