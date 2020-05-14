lst = [1,3,2,3,5,0]
lst = [1,2,3]
lst = [1,1,3,3,5,5,7,7]
lst = [1,2,3,1,1,4,0]
ha = {}
cnt=0
for i in lst:
    if ha.get(i,None) != None:
        ha[i] = ha[i]+1
        cnt+= 1 if ha.get(i+1,0) else 0
    else:
        cnt+=ha.get(i-1,0)
        cnt+=1 if ha.get(i+1,0) else 0
        ha[i] = 1
print(cnt)