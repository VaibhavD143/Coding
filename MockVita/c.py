arr = []
dep = []
for _ in range(int(input())):
    a,d = map(int,input().split())
    arr.append(a)
    dep.append(a+d)
arr.sort(reverse = True)
dep.sort(reverse = True)
res = 0
cnt = 0
while arr and dep:
    if arr[-1]<=dep[-1]:
        arr.pop()
        cnt+=1
    else:
        dep.pop()
        cnt-=1
    res = max(res,cnt)
print(res)