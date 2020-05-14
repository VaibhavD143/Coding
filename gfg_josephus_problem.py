"""
https://practice.geeksforgeeks.org/problems/josephus-problem/1
"""

def find_it(n,k):
    
    if n==1:
        return 1
    
    return (find_it(n-1,k)+k-1)%n+1


for _ in range(int(input())):
    n,k = map(int,input().split())
    print(find_it(n,k))