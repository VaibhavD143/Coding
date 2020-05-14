a= [2,3,5,1,7]
b = [7,2,5,6,1]
a=[1,2,3]
b=[1,2,3]

ha={}
for i,val in enumerate(a):
    ha[val]=i
hdiff = {}
cnt=0
for i,val in enumerate(b):
    pos = ha.get(val,-1)
    if pos !=-1:
        hdiff[(i-pos)%len(a)]=1+hdiff.get((i-pos)%len(a),0)
    else:
        cnt+=1
print(ha)
print(hdiff)
res = len(a)
rem = 0
for i,j in hdiff.items():
    rem = max(rem,j-i)
print(rem)
print(res-rem)