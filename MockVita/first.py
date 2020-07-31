from collections import Counter
n = int(input())
b = input()
g = input()
cb = Counter(b)
cg = Counter(g)
brum = cb['r']
bmoi = cb['m']
grum = cg['r']
gmoi = cg['m']
if brum == grum and bmoi == gmoi:
    print(0)
elif bmoi>gmoi:
    diff = gmoi
    i=0
    while diff>=0:
        if b[i] == 'm':
            diff-=1
        i+=1
    print(n-i+1)
else:
    diff = grum
    i=0
    while diff>=0:
        if b[i] == 'r':
            diff-=1
        i+=1
    print(n-i+1)
