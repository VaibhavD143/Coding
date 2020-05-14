intervals = [[3,5],[6,7],[8,10],[13,16]]
newInterval = [9,15]
# newInterval = [9,11]
# newInterval = [11,15]
# newInterval = [17,19]
# newInterval = [15,19]
# newInterval = [1,2]
# newInterval = [1,4]
# newInterval = [1,1]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

ind = 0
res = []
while ind < len(intervals) and newInterval[0] >intervals[ind][0]:
    res.append(intervals[ind])
    ind+=1

if not len(res):
    res.append(newInterval)
else:
    if newInterval[0] <= res[-1][1]:
        res[-1][1] = max(newInterval[1],res[-1][1])
    else:
        res.append(newInterval)

print(res,ind)

while ind<len(intervals) and res[-1][1] >= intervals[ind][0]:
    res[-1][1] = max(intervals[ind][1],res[-1][1])
    ind+=1
else:
    res.extend(intervals[ind:])
print(res)

