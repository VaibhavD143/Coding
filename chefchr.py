tc = int(input())
while tc:
	st = input()
	cnt = 0
	if len(st) < 4:
		print("normal")
		tc-=1
		continue
	for i in range(len(st)-3):
		lst = ['c','f','h','e']
		try:
			lst.remove(st[i])
			lst.remove(st[i+1])
			lst.remove(st[i+2])
			lst.remove(st[i+3])
		except:
			pass
		if len(lst) == 0:
			cnt+=1
	if cnt:
		print("lovely",cnt)
	else:
		print("normal")
	tc = tc-1