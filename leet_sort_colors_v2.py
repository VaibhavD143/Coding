lst = [2,0,2,1,1,0]
# lst=[2,2,1,2,0]
# lst= [2,0,    2,2]
lst = [2,0,1]
i0=0
i2=len(lst)-1
i = 0
while i <= i2:
    if lst[i] == 2:
        lst[i],lst[i2] = lst[i2],lst[i]
        i2-=1
    elif lst[i] == 0:
        lst[i],lst[i0]=lst[i0],lst[i]
        i0+=1
        i+=1
    else:
        i+=1
print(lst)