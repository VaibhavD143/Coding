"""
Intution : 
Read on digit dp
and just travers from left to right
"""
import math
n = int(input())
# n = 177
sn = str(n)
maxSum = 9*len(sn)
dp = [[[[None for _ in range(2)] for _ in range(20)] for _ in range(maxSum)] for _ in range(len(sn))]

isPrime = [True]*(maxSum+1)
def checkPrime():
    isPrime[0] = False
    isPrime[1] = False
    isPrime[2] = True
    for i in range(2,int(len(isPrime)**0.5)+1):
        if isPrime[i]:
            for j in range(i+i,len(isPrime),i):
                isPrime[j] = False

def rec(pos,sm,xor,bound):
    if pos == len(sn):
        if xor == 1 and not isPrime[sm]:
            print(sm)
            return 1
        return 0
    
    if dp[pos][sm][xor][bound] != None:
        return dp[pos][sm][xor][bound]

    hi=9
    if bound:
        hi = int(sn[pos])
    
    res = 0
    for i in range(hi):
        res+=rec(pos+1,sm+i,xor^i,0)
    res+=rec(pos+1,sm+hi,hi^xor,bound)

    dp[pos][sm][xor][bound] = res
    return res
checkPrime()
print(isPrime)
print(rec(0,0,0,1))