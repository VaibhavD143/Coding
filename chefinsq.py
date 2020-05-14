"""
https://www.codechef.com/SEPT19B/problems/CHEFINSQ
"""
def nCr(n, r): 

    return (fact(n) // (fact(r)  
            * fact(n - r))) 

def fact(n): 

    res = 1
        
    for i in range(2, n+1): 
        res = res * i 
            
    return res 

for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    i=0
    j=1
    cnt_k=1
    ans = 1
    # while cnt_k<=k and j <= k:
    #     s_cnt = 1
    #     while lst[i] == lst[j]:
    #         j+=1
    #         s_cnt+=1
    #     i=j
    #     j+=1
    #     cnt_k+=1
    #     ans *= s_cnt

    while i< k:
        cnt_sm=1
        while j<n and lst[i] == lst[j]:
            j+=1
            cnt_sm+=1
        i=j
        j+=1
        ans=cnt_sm    
    print(nCr(ans,ans-i+k))
    print(ans,i,j,k)
    # cnt = 0
    # i=k-1
    # j=k
    # while j<n and lst[i] == lst[j]:
    #     cnt+=1
