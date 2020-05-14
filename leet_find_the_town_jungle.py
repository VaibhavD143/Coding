from collections import Counter

lst =  [[1,3],[1,4],[2,3],[2,4],[4,3]]
N = 4
cnt2 = Counter(map(lambda item: item[1],lst))
cnt1 = Counter(map(lambda item: item[0],lst))
for i,val in cnt2.items():
    if val == N-1 and not cnt1[i]:
        print(i)
        exit(1)
print(-1)