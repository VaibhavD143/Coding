tc = int(input())
while tc:
	t = int(input())
	tms = list(map(int,input().strip().split()))
	c,d,v= map(int,input().strip().split())
	dis_time = d/v
	effective = max(tms)
	ans = (c-1)*effective
	print(ans)
	tc-=1