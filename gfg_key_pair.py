"""
https://practice.geeksforgeeks.org/problems/key-pair/0
if array contains two elements x,y wehre x+y=k
"""
import math

for _ in range(int(input())):
    n,k = map(int,input().split())
    
    lst = list(map(int,input().split()))
    hash = {}
    for i in lst:
        num = hash.get(i,0)
        hash[i] = num+1
    flag = 0
    for i in lst:
        hash[i]-=1
        try:
            if hash[k-i]:
                print(i,k-i)
                flag = 1
                break
        except:
            pass
        hash[i]+=1
    if flag:
        print("Yes")
    else:
        print("No")