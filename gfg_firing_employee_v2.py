"""
https://practice.geeksforgeeks.org/problems/firing-employees/0/?track=sp-trees&amp;batchId=152
"""

def cnt(rank,sen_cnt,rank_lst):

    if sen_cnt[rank-1] != -1:
        return sen_cnt[rank-1]
    if rank == 0:
        return 0   

    sen_cnt[rank-1] = 1+cnt(rank_lst[rank-1],sen_cnt,rank_lst)
    return sen_cnt[rank-1]
n = 100000
prime = [1]*(2*n+1)
prime[0] = 0
# prime[2] = 0
for i in range(2,n+1):
    for j in range(2,n):
        ind = i*j
        if ind< 2*n+1:
            prime[ind]=0
        else:
            break

for _ in range(int(input())):
    n = int(input())
    rank_lst = list(map(int,input().split()))
    if n == 1:
        print(0)
        continue
    
    sen_cnt = [-1]*n
    for i in range(n):
        if sen_cnt[i] == -1:
            stack = [i]
            while sen_cnt[stack[-1]] == -1 and rank_lst[stack[-1]] != 0:
                stack.append(rank_lst[stack[-1]]-1)
            if rank_lst[stack[-1]] == 0:
                sen_cnt[stack.pop()] = 1
            else:
                stack.pop()
            while stack:
                sen_cnt[stack[-1]] = sen_cnt[rank_lst[stack[-1]]-1]+1
                stack.pop()
    # print(list(range(n)))
    # print(rank_lst)
    # print(sen_cnt)
    
    
    
    # print(list(range(2*n+1)))
    # print(prime)
    res=0
    for i in range(n):
        if prime[sen_cnt[i]+i] and rank_lst[i]:
            # print(i)
            res+=1
    print(res)