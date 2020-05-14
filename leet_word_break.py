s = "leetcode"
# s = "applespenapple"
# s = "catsandog"
wordDict = ["leet", "code"]
# wordDict = ["apple","apples", "pen"]
# wordDict = ["cats", "dog", "sand", "and", "cat"]
dp = [[-1]*len(s) for _ in range(len(s))]

def pr(dp):
    for row in dp:
        print(row)

def fun(s,start,end,dp,wordDict):
    if dp[start][end] != -1:
        return dp[start][end]
    print(start,end)
    
    dp[start][end] = False

    if s[start:end+1] in wordDict:
        dp[start][end] = True
        return True
    
    for i in range(start,end+1):
        # if s[start:i+1] in wordDict:
        #     dp[start][i] = True
        #     dp[start][end] = dp[start][end] or fun(s,i+1,end,dp,wordDict)
        if fun(s,start,i,dp,wordDict) and fun(s,i+1,end,dp,wordDict):
            dp[start][i] = True
            dp[i+1][end] = True
            dp[start][end] = True
            return dp[start][end]
        
    return dp[start][end]

print(fun(s,0,len(s)-1,dp,wordDict))
pr(dp)
