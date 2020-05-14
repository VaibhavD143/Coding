lst = [3,5,7,2,4,8,5,3]
lst = [1]
l_lst = len(lst)
ss = []
maxArea = 0
for i in range(0,l_lst):
    tcnt =0
    while ss and lst[ss[-1][0]]>lst[i]:
        elem= ss.pop()
        maxArea = max(maxArea,lst[elem[0]]*(elem[1]+i-elem[0]))
        tcnt += elem[1]+1
    ss.append([i,tcnt])
    print(ss)
while ss:
    elem= ss.pop()
    maxArea = max(maxArea,lst[elem[0]]*(elem[1]+l_lst-elem[0]))
print(maxArea)