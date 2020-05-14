#https://practice.geeksforgeeks.org/problems/max-length-chain/1

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    lst_itr = iter(lst)
    pairs = [[x,next(lst_itr)] for x in lst_itr]
    pairs.sort(key=lambda x: x[1])
    cnt = 1
    c_no = pairs[0][1]
    for pair in pairs[1:]:
        if c_no<pair[0]:
            cnt+=1
            c_no = pair[1]
    print(cnt)