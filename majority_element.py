#find the element which repeats more than n/2 times in the array

lst = [2,2,1,2,53,2]
x = lst[0]
cnt =0
l_lst = len(lst)
for i in range(len(lst)):
    if x == lst[i]:
        cnt+=1
    else:
        if cnt == 0:
            x = lst[i]
            cnt = 1
        else:
            cnt-=1
cnt=0
for i in range(l_lst):
    if lst[i] == x:
        cnt+=1

if cnt >= l_lst/2:
    print(x,cnt)
else:
    print("No majority element")