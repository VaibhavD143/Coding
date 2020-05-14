# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    s = (n*(n+1))//2
    print(s-sum(lst))