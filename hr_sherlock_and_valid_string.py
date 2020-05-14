string = input()
cnt = [0]*27
for i in string:
	cnt[ord(i)-ord('a')] += 1
# flag = 0
# first = cnt[0]
# second = -1
freq = {}
for i in range(0,27):
	if cnt[i] not in freq:
		freq[cnt[i]] =1
	else:
		freq[cnt[i]] += 1
if(len(freq) > 3 ):
	print('NO')
else:
	flag = 0
	flag_key = 0
	# print(type(freq)) 
	for key,val in freq.items():
		if key == 0:
			pass
		else:
			if flag_key == 0:
				first = key
				second = key
				flag_key = 1
			else:
				second = key
			if val > 1 and flag == 0:
				flag = 1
			elif val > 1 and flag == 1:
				print('NO')
				break
	else:
		del freq[0]
		first = list(freq.keys())[list(freq.values()).index(min(freq.values()))]
		second = list(freq.keys())[list(freq.values()).index(max(freq.values()))]
		if(first - second) in [0,1] or min(freq.keys()) == 1:
			print('YES')
		else:
			print('NO')