A=[6,7,8,9,10]
l=0
r=len(A)-1
l_elm = A[0]
while l<r:
    mid = (l+r)//2
    
    if l_elm<A[mid] :
        l=mid+1
    else:
        r=mid
print(A)
print(l,mid,r)