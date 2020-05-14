def find_expo(bas,expo,mod):
	temp = 1
	while expo>0:
	
		if expo%2:
			temp = (temp*bas)%mod
		bas = (bas*bas)%mod
		expo = expo//2
	return temp%mod

print(find_expo(2,7,10005),(2**7)%10005)