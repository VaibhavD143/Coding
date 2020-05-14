"""
https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game/0
"""

def find_max_coins(s_ind,e_ind,lst,turn):
    global dp
    if dp[s_ind][e_ind] != [None,None]:
        return dp[s_ind][e_ind]

    if s_ind == e_ind:
        if turn ==0:
            dp[s_ind][e_ind] = [lst[s_ind],0]
        else:
            dp[s_ind][e_ind] = [0,lst[s_ind]]
        return dp[s_ind][e_ind]
    
    l_p1,l_p2 = find_max_coins(s_ind+1,e_ind,lst,1-turn)
    r_p1,r_p2 = find_max_coins(s_ind,e_ind-1,lst,1-turn)

    if turn == 0:
        l_p1+=lst[s_ind]
        r_p1+=lst[e_ind]
        if l_p1 > r_p1:
            dp[s_ind][e_ind] = [l_p1,l_p2]
            return dp[s_ind][e_ind] 
        dp[s_ind][e_ind] = [r_p1,r_p2]
        return dp[s_ind][e_ind] 
    l_p2+=lst[s_ind]
    r_p2+=lst[e_ind]
    if l_p2>r_p2:
        dp[s_ind][e_ind] = [l_p1,l_p2]
        return dp[s_ind][e_ind] 
    dp[s_ind][e_ind] = [r_p1,r_p2]
    return dp[s_ind][e_ind] 

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    dp = [[[None,None]]*n for _ in range(n)]
    print(find_max_coins(0,n-1,lst,0)[0])