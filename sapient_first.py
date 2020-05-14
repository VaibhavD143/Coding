n = int(input())
tc = n
mat = []
while tc:
	str = list(map(int,input().split()))
	mat.append(str)
	tc = tc -1
ans = []
for i in range(n):
	flag = 0
	for j in range(n):
		if mat[i][j] == 1 or mat[i][j] == 3:
			flag =1
			break
	if flag == 0:
		ans.append(i+1)
print(len(ans))
if len(ans) > 0:
	print(*ans)