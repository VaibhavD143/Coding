"""
https://practice.geeksforgeeks.org/problems/combination-sum-part-2/0
"""

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    k = int(input())
    res = [set() for i in range(k+1)]
    lst.sort()
    for i in lst:
        for j in range(k,0,-1):
            for x in res[j]:
                if i+j > k:
                    break
                res[i+j].add(x+(i,))
        if i<=k:
            res[i].add((i,))
    
    if res[-1]:
        for i in res[-1]:
            if len(i) == 1:
                print('('+str(i[0])+')')
                continue
            print('('+' '.join(str(x) for x in i)+')',end="")
        print()
    else:
        print("Empty")
