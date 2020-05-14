n = int(input())

lst = sorted(list(map(int,input().split())))
sum = cnt = 0
ans = []

for i in range(n):
	if lst[i] < sum:
		ans.append(lst[i])
		cnt += 1
	else:
		sum += lst[i]
print(n-cnt)
