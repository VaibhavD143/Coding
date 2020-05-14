import math
m = 16
n = 16
# if m == n:
#     print(m)
#     exit(1)
if int(math.log2(m)) != int(math.log2(n)):
    print(0)
    exit(1)
pw = int(math.log2(m))
binm = bin(m)[2:]
binn = bin(n)[2:]
res = 0
print(binm,binn)
for i,j in zip(binm,binn):
    print(i,j)
    if i != j :
        print(res)
        exit(1)
    if i == '1':
        res += 2**pw
    pw-=1
print(res)