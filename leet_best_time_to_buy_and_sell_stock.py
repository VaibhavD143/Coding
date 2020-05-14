prices = [7,1,5,3,6,4]
if not prices:
    return 0
st = prices

ss = []
r = len(st)-1
ss.append([r,st[-1]])

while r>=0:
    if ss[-1][1] < st[r]:
        ss.append([r,st[r]])
    r-=1
max_diff = 0
for i in range(len(st)):
    while ss[-1][0]<i:
        ss.pop()
    max_diff = max(max_diff,ss[-1][1]-st[i])

print max_diff