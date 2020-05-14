from collections import Counter
s = "loveleetcode"
cnt = Counter(s)
for i,v in enumerate(s):
  if cnt[v] == 1:
    print(i)
    exit(1)
print(-1)
