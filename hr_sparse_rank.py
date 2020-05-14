n = int(input())
lst = []
while n:
	key=input()
	lst.append(key)
	n-=1
n= int(input())
while n:
	key = input()
	print(lst.count(key))
	n-=1