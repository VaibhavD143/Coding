def gcd(a,b):
	a,b = max(a,b),min(a,b)
	while  b:
		a,b = b,a%b
		print(a,b)
	return a

def lcm(a,b):

	return a*b // gcd(a,b)
