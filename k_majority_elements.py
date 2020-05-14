#find elements which repeats n/k times in the list

lst = [2,53,1,4,2,2,2,1,1,1]
l_lst = len(lst)
k = 3
bucks = [None]*(k-1)
cnt = [0]*(k-1)

def add_elem(elem,bucks,cnt,l_cnt):
    for j in range(l_cnt):
        if bucks[j] == elem:
            cnt[j]+=1
            return
    for j in range(l_cnt):
        if bucks[j] == None:
            bucks[j] = elem
            cnt[j]=1
            return
    for j in range(l_cnt):
        cnt[j] = cnt[j]-1
        if cnt[j] < 1:
            cnt[j] = 0
            bucks[j] = None
            return

for i in range(l_lst):
    add_elem(lst[i],bucks,cnt,k-1)
flag = 0
for cand in bucks:
    cnt=0
    for j in range(l_lst):
        if lst[j] == cand:
            cnt+=1
    if cnt> l_lst//k:
        print("No : ",cand)
        flag = 1
if not flag:
    print("No majority elem")