lst = [2,3,1,1,4]
lst = [3,2,1,0,4]
# dp = [0]*len(lst)
max_ind = 0
for i in range(len(lst)):
    if i <= max_ind:
        max_ind = max(lst[i]+i,max_ind)
        print(i,max_ind)
if max_ind >= len(lst)-1:
    print(1)
else:
    print(0)