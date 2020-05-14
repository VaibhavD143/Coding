import time
# lst = [i for i in range(20000)]
lst = [0,0,0,0,0,0,0,0,0,0]

k=0

# lst = [1,-1,1]
# k=1
# lst = [4,5,9,-18]
# k=0

if not lst:
    print(0)
cnt=0

sm = 0
hm = {}

for i in range(len(lst)):
    sm = sm+lst[i]
    if sm == k:
        cnt+=1
    if hm.get(sm-k,-1) != -1:
        cnt+=hm[sm-k]

    hm[sm] = hm.get(sm,0)+1
    print(hm)
print(cnt)