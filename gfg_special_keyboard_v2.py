"""
https://practice.geeksforgeeks.org/problems/special-keyboard/0
solution : https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/
"""
from collections import deque

for _ in range(int(input())):
    n = int(input())
    if n <7:
        print(n)
        continue
    
    prev_5 = deque([2,3,4,5,6])
    res = 0
    for i in range(7,n+1):
        res = max(prev_5[0]*4,prev_5[1]*3,prev_5[2]*2)
        prev_5.popleft()
        prev_5.append(res)
    
    print(res)