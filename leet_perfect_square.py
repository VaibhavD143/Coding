import math
n = 4
nos = []
for i in range(1,math.ceil(math.sqrt(n))+1):
    nos.append(i**2)
print(nos)
print(math.ceil(math.sqrt(n)))
path = [n]*(n+1)
path[0] = 0
for no in  nos:
    
    for i in range(n-no+1):
        print(i+no)
        path[i+no] = min(path[i]+1,path[i+no])
    
print(path)