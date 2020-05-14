if __name__ == '__main__':
	n,m = map(int,input().split())
	lst = [0]*n

	while m:
		a,b,c = map(int,input().split())
		lst[a-1] += c
		try:
			lst[b] -= c
		except IndexError:
			pass
		m-=1

	max_cnt = 0
	cnt = 0
	for i in range(n):
		cnt += lst[i]
		max_cnt = max(cnt,max_cnt)
		lst[i] = cnt
	print(max_cnt)