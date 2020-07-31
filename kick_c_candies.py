def update(bit,ind,val):
    ind+=1
    while ind<len(bit):
        bit[ind]+=val
        ind += ind&-ind

def getSum(bit,ind):
    ind+=1
    res=0
    while ind:
        res+=bit[ind]
        ind-=(ind&-ind)
    return res
    
def que(bit,l,r):
    return getSum(bit,r)-getSum(bit,l-1)    

for tc in range(int(input())):
    n,q = map(int,input().split())
    
    bit1 = [0]*(n+1)
    bit2 = [0]*(n+1)
    lst = list(map(int,input().split()))
    for i,n in enumerate(lst):
        # print(n,end=" ")
        update(bit1,i,(-1 if i&1 else 1)*n)
        update(bit2,i,(-(i+1) if i&1 else (i+1))*n)
    # print()
    res = 0
    for _ in range(q):
        s,l,r = input().split()
        l,r = int(l),int(r)
        if s=='Q':
            l-=1
            r-=1
            val=(-1 if l&1 else 1)*(que(bit2,l,r)-(l)*que(bit1,l,r))
            res+=val
            # print(val)
        else:
            l-=1
            # print(l,r,'-------')
            val1 = (-1 if l&1 else 1)*(r- lst[l])
            # print(val1)
            # val1 = val1 - lst[l]
            # print(val1)
            update(bit1,l,val1)
            val2 = (-(l+1) if l&1 else (l+1))*(r-lst[l])
            # val2 = val2 - lst[l]
            update(bit2,l,val2)
            # print(que(bit1,1,1))
            # print(que(bit2,1,1))
            # print(que(bit1,l,l))
            # print(que(bit2,l,l))
            lst[l] = r
    
    print(F'Case #{tc}: {res}')