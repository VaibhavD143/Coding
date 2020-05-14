"""
https://leetcode.com/problems/combination-sum/
"""

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    k = int(input())
    res = [set() for i in range(k+1)]
    lst.sort()
    for i in lst:
        for j in range(k+1):
            for x in res[j]:
                if i+j > k:
                    break
                res[i+j].add(x+(i,))
        mulp = 1
        while (i*mulp)<=k:
            res[i*mulp].add((i,)*mulp)
            mulp+=1
    
    print(res[-1])