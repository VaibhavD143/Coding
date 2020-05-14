# find rank by grouping it into group of 5

# find first max k elements
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
# lst = list(range(int(1e6),0,-1))
# lst= list(range(100,0,-1))
# lst = [2, 38, 23, 52, 57, 1, 33, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
lst = [1,2,3,4,5,6]
ind = find_rank(lst,0,len(lst),5)
# print(lst)
# ind = pivot(lst,64,100)
# print(ind,lst[ind])
# print(lst)
end = time.time()
print(end-start)
print(ind)