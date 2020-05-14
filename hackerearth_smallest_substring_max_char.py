lst = list(input())
ha = {}

for i in lst:
    ha[i]=ha.get(i,0)+1
l,r=0,len(lst)-1
for l in range(len(lst)):
    if ha[lst[l]] == 1:
        break
    ha[lst[l]]-=1
for r in range(len(lst)-1,l,-1):
    if ha[lst[r]] == 1:
        break
    ha[lst[r]]-=1
ans1 = r-l+1
ha = {}
for i in lst:
    ha[i]=ha.get(i,0)+1
l,r=0,len(lst)-1
for r in range(len(lst)-1,l,-1):
    if ha[lst[r]] == 1:
        break
    ha[lst[r]]-=1
for l in range(len(lst)):
    if ha[lst[l]] == 1:
        break
    ha[lst[l]]-=1
ans2 = r-l+1
print(min(ans1,ans2))