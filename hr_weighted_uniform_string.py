# def factors(n):
#     return list(set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup))
# string = input()
# que = int(input())
# cnt = {}
# # print(string)
# for i in set(string):
# 	cnt[ord(i)-ord('a')+1] = 0
# for j in string:
# 	cnt[ord(j)-ord('a')+1] += 1
# # print(cnt)
# while que:
# 	# print('-------------------------------------------------')
# 	no = int(input())
# 	fact =factors(no)
# 	# print(no,fact)
# 	if no == 0 :
# 		print('Yes')
# 		que -= 1
# 		continue
# 	# print(fact)
# 	for i in fact:
# 		if i in cnt:
# 			# print('in')
# 			if cnt[i] >= no/i:
# 				# print(cnt[i],no,i)
# 				print('Yes')
# 				break
# 	else:
# 		print('No')
# 	que -= 1
#!/bin/python3
import sys
from itertools import groupby

alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

d = set()

s = input().strip()
n = int(input().strip())

for key , group in groupby(s):
    k = (len(list(group)))
    if(k > 1 ):
        for j in range(k,0,-1):
            d.add(alpha[key]*j)
    else:
        d.add(alpha[key])
        
for a0 in range(n):
    x = int(input().strip())
    if x in d:
        print("Yes")
    else:
        print("No")