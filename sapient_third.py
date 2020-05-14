n = int(input())
tn = n
lst = [] 
while tn:
	x,h = map(int,input().split())
	lst.append([x,h])
	tn-=1

cnt = 1	#first tree to the left of it
pre = 'l'
for i in range(1,len(lst)-1):
	# print(i,lst[i])
	if pre == 'l':
		# print(lst[i][0]-lst[i-1][0] ,lst[i][1],'l',cnt)
		if lst[i][0]-lst[i-1][0] > lst[i][1]:
			pre = 'l'
			cnt += 1
			continue
	if pre == 'r':
		# print(lst[i][0]-(lst[i-1][0]+lst[i-1][1]) ,lst[i][1],'r',cnt)
		if lst[i][0]-(lst[i-1][0]+lst[i-1][1]) > lst[i][1]:
			pre = 'l'
			cnt += 1
			continue
	if lst[i][1] < lst[i+1][0] - lst[i][0]:
		# print(lst[i+1][0] - lst[i][0] ,lst[i][1],cnt)
		pre = 'r'
		cnt += 1
		continue
	else:
		pre == "n"
if len(lst) > 1 :
	cnt+=1
print(cnt)