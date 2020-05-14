tc= int(input())
while tc:
	n,m,x,k = map(int,input().strip().split())
	st = input()
	even = st.count('E')
	odd = k - even
	flag = 0
	if n > k:
		print("no")
		tc-=1
		continue
	for i in range(1,m+1):
		if i%2:
			tasks=min(x,odd)
			n-=tasks
			odd-=tasks
		else:
			tasks=min(x,even)
			n-=tasks
			even-=tasks
		if n<1 :
			flag = 1
			break
		if odd<1 and even < 0:
			flag = 0
			break
	if flag:
		print("yes")
	else:
		print("no")
	tc-=1
	# even_months = even // x
	# odd_months = odd // x
	# if not even_months == even/x:
	# 	even += 1
	# if not odd_months == odd/x:
	# 	odd += 1
