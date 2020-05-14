def find_expo(bas,expo):
	temp = 1
	while expo>0:
	
		if expo%2:
			temp = (temp*bas)
		bas = (bas*bas)
		expo = expo//2
	return temp

for _ in range(input()):
  l,r = map(int,input().split())
  lst1=list(map(int,input().split()))
  lst2=list(map(int,input().split()))
  cnt=0
  for i in lst1:
    for j in lst2:
      if find_expo(i,j) > find_expo(j,i):
        cnt+=1
  print(cnt)