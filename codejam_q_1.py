tc= int(input())

def count_damage(st):
	cnt = 1
	dmg = 0
	for i in st:
		if i == 'C':
			cnt*=2
		else:
			dmg+=cnt
	return cnt

while tc:
	d,st = input().strip().split()
	d = int(d)
	no_s = st.count('S')
	if no_s > d:
		print('IMPOSSIBLE')
		tc-=0
		continue

	while count_damage(st) > d:
		for j in range(1,len(st)):
			if st[j] == 'S':


	tc-=1