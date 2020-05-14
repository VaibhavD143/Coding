def find_expo(bas,expo):
	temp = 1
	while expo!=0:
	
		if expo%2:
			temp = (temp*bas)
		bas = (bas*bas)
		expo = int(expo/2)
	return temp

print(find_expo(2.5,-6))