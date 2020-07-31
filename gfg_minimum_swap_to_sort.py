"""
Intution:

"""
def minSwaps(arr, N):
    # Code here
    ind = {}
    for i,val in enumerate(sorted(arr)):
        if val in ind:
            ind[val].append(i)
        else:
            ind[val]=[i]
    # print(ind)
    i=res=0
    while i<len(arr):
        # print(i,arr[i],ind)
        if not ind[arr[i]]:
            i+=1
            continue
        if ind[arr[i]][-1]==i:
            ind[arr[i]].pop()
            i+=1
            continue
        else:
            actual = ind[arr[i]].pop()
            if arr[actual]==arr[i]:
                i+=1    
                continue
            arr[actual],arr[i] = arr[i],arr[actual]
            res+=1
            
    return res