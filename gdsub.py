n,k = map(int,input().split())
lst = list(map(int,input().split()))
cnt = {}
l_cnt = 0
for i in range(n):
    try:
        cnt[lst[i]]+=1
    except:
        cnt[lst[i]]=1
        l_cnt+=1

cnt = list(cnt.values())
print(cnt)
postfix_sum = [0]*l_cnt
postfix_sum[l_cnt-1] = cnt[-1]
for i in range(l_cnt-2,-1,-1):
    postfix_sum[i] = postfix_sum[i+1]+cnt[i]
res = 1 #zero length sequence
if k>l_cnt:
    nonz_res=1
    for i in range(l_cnt):
        nonz_res*=(cnt[i]+1)
    nonz_res-=1
    res+=nonz_res
else:
    res+=postfix_sum[0]
    print(res)
    for i in range(1,k):
        for j in range(l_cnt-i):
            mulp = 1
            for k in range(j,j+i):
                mulp*=cnt[k]
            res+=(mulp*postfix_sum[j+1])
        print(res)
            
print(res)