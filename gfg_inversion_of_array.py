"""
Find the no of occurance when i<j and a[i]>=a[j](Inversion)
aproach : increase count when merging in mergesort function
"""

count = 0
def merge(lst,l,r):
    global count
    mid =l+ (r-l)//2
    lp = l
    rp = mid+1
    tlst=lst[l:r+1]
    ind =l
    while lp<=mid and rp<=r:
        if tlst[lp-l]<tlst[rp-l]:
            lst[ind] = tlst[lp-l]
            lp+=1
        else:
            count+=(mid-lp+1)   #because all the elements of first array[lp:mid+1] are greater so add them at once
            lst[ind]=tlst[rp-l]
            rp+=1
        ind+=1
    while lp<=mid:
        lst[ind] = tlst[lp-l]
        lp+=1
        ind+=1
    
    while rp<=r:
        lst[ind] = tlst[rp-l]
        rp+=1
        ind+=1

def mergeSort(lst,l,r):
    if l >= r:
        return

    mid = l+(r-l)//2
    # print(l,r)
    mergeSort(lst,l,mid)
    mergeSort(lst,mid+1,r)
    merge(lst,l,r)
lst = [2,3,4,2,1]
mergeSort(lst,0,len(lst)-1)
print(lst)
print(count)