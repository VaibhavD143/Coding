"""
https://practice.geeksforgeeks.org/problems/special-keyboard/0
TLE
"""
def max_A(cnt,n,buff):
    
    if n == 0:
        return cnt

    return max(max_A(cnt+1,n-1,buff),max_A(cnt*2,n-3,cnt) if n>2 else cnt,max_A(cnt+buff,n-1,buff) if buff else cnt)

for _ in range(int(input())):
    n = int(input())
    print(max_A(0,n,0))