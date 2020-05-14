# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
#TLE

def find_sum(arr,l,sm):
    if l < 2:
        return max(sm+arr[0],sm,arr[0])
    
    return max(find_sum(arr[1:],l-1,sm+arr[0]),find_sum(arr[1:],l-1,arr[0]),sm)


    
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    print(find_sum(lst[1:],n-1,lst[0]))