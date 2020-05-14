def merge(lst,l,r):
    mid = (r-l)//2
    lp = l
    rp = mid+1
    tlst=lst[l:r+1]
    ind =l
    while lp<=mid and rp<=r:
        if tlst[lp]<tlst[rp]:
            lst[ind] = tlst[lp]
            lp+=1
        else:
            lst[ind]=lst[rp]
            rp+=1
        ind+=1
    
    while lp<=mid:
        lst[ind] = tlst[lp]
        lp+=1
        ind+=1
    
    while rp<=r:
        lst[ind] = tlst[rp]
        rp+=1
        ind+=1
    
def mergeSort(lst,l,r):
    if l >= r:
        return

    mid = (r-l)//2

    mergeSort(lst,l,mid)
    mergeSort(lst,mid+1,r)
    merge(lst,l,r)
lst = [1,3,4,2,5]
merge(lst,0,4)
print(lst)