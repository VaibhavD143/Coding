# find first max k elements from n elements where n>m

import time
import math

def pivot(arr,left,right):
    #left inclusive and right exclusive
    if (right - left) < 6:
        arr[left:right] = sorted(arr[left:right])
        return left+((right-left)//2)
    

    for i in range((right-left)//5):
        arr[left+i*5:left+i*5+5] = sorted(arr[left+i*5:left+i*5+5])
        arr[left+i],arr[left+i*5+2] = arr[left+i*5+2],arr[left+i]
        # print('-----------------------------------------',left+i*5,left+i*5+5)
        # print(arr)
        # print('-----------------------------------------')
        
    if (right-left)%5:
        i+=1
        arr[left+i*5:] = sorted(arr[left+i*5:])
        arr[left+i],arr[left+i*5+((right-left)%5)//2] = arr[left+i*5+((right-left)%5)//2],arr[left+i]
        # print('-----------------------------------------',left+i*5,left+i*5+((right-left)%5))
        # print(arr)
        # print('-----------------------------------------')
    # print('*******************************************')
    # print(arr)
    # print('*******************************************')
    # return
    return pivot(arr,left,left+i+1)
    
def find_rank(arr,left,right,rank):
    ind = pivot(arr,left,right)
    arr[left],arr[ind] = arr[ind],arr[left]

    print(ind,left,right,rank)

    first = left
    for second in range(left+1,right):
        if arr[left] >= arr[second]:
            first+=1
            arr[first],arr[second] = arr[second],arr[first]
    arr[left],arr[first] = arr[first],arr[left]
    

    if right-first == rank:
        return first
    elif right-first < rank:
        return find_rank(arr,left,first,rank-right+first)
    else:
        return find_rank(arr,first+1,right,rank)

start = time.time()

lst = list(range(int(1e6),0,-1))
n = int(1e6)
m = int(1e4)

ind = find_rank(lst,0,n,n)
print(ind,lst[ind])
end = time.time()
print(end-start)