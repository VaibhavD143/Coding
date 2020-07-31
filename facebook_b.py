from collections import Counter
for _ in range(int(input())):
    n = int(input())
    cnt = Counter(input())
    res = 'Y' if abs(cnt['A']-cnt['B'])==1 else 'N'
    print(F'Case #{_+1}: {res}')
