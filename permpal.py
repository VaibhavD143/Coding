from collections import defaultdict

if __name__ == '__main__':
	tc = int(input())
	while tc:
		st = input()
		l = len(st)
		abcd = [0]*26
		for i in st:
			abcd[ord(i)-ord('a')]+=1
		flag = 0
		for j in range(26):
			if abcd[j]%2:
				odd = chr(j+ord('a'))
				flag+=1
		if l%2 == 0 and flag != 0 or flag > 1:
			print('-1')
			tc-=1
			continue

		d = defaultdict(list)
		
		for i in range(l):
			d[st[i]].append(i+1)

		ans = [0]*l
		ind = 0
		if flag:
			odd_key = d[odd][:]
			odd_len = abcd[ord(odd)-ord('a')]
			for i,j in d.items():
				# print(i,j)
				half = (abcd[ord(i)-ord('a')]//2)
				for k in range(half):
					ans[ind] = j[k]
					ans[l-ind-1] = j[k+half]
					ind+=1
			ans[ind] = odd_key[-1]
		else:
			for i,j in d.items():
				# print(i,j)
				half = (abcd[ord(i)-ord('a')]//2)
				for k in range(half):
					ans[ind] = j[k]
					ans[l-ind-1] = j[k+half]
					ind+=1
			
		print(*ans)
		tc-=1
