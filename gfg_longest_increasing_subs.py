#Look at ib's solution
def inc_subs(lst,ind,pre):
    global dp    
    if ind >=len(lst):
        return 0
    
    in_seq=0
    if dp[ind][pre] != -1:
        return dp[ind][pre]
    if pre == -1 or lst[ind] > lst[pre]:
        in_seq = inc_subs(lst,ind+1,ind)+1
    
    out_seq = inc_subs(lst,ind+1,pre)
    dp[ind][pre] = max(in_seq,out_seq)
    return dp[ind][pre]

# for _ in range(int(input())):
# n = int(input())

# lst = list(map(int,input().split()))
lst = [0,8,4]
dp = [[-1]*(len(lst)) for i in range(len(lst))]
print(inc_subs(lst,0,-1))
