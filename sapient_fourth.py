def computeHCF(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y

   return x

# print(computeHCF(6, 4))

n,x,y = map(int,input().split())
gcd = computeHCF(x,y)
x = int(x/gcd)
y = int(y/gcd)
lstS = [[float(i/x),'S'] for i in range(1,x+1)]
lstM = [[float(i/y),'M'] for i in range(1,y+1)]
lst = sorted(lstS+lstM)

while n:
	a = int(input())
	a1 = (a+1) % (x+y)
	a = a % (x+y)
	if a == 0 or a1 == 0:
		print("Both")
	else:
		if lst[a-1][1] == 'S':
			print("Sonu")
		elif lst[a-1][1] == 'M':
			print("Monu")
	n-=1