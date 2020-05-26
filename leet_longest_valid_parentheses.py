"""
Intution:
dp[i] = stores length of valid parentheses ending on ith index
if ith index is '(' => 0
                ')' => skip valid string length stored in dp[i-1] if match then add that string(i-ind+1)+string before that (if any,dp[ind-1])
$ to avoid out of index check
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = '$'+s
        dp = [0]*len(s)
        
        for i in range(1,len(dp)):
            if s[i] == '(':
                dp[i]=0
            else:
                diff = dp[i-1]
                ind = i-diff-1
                if s[ind] == '(':
                    dp[i] = (i-ind+1)+dp[ind-1]
                else:
                    dp[i]=0
        return max(dp)

"""
left to right scan method from solution
"""

lst = "(((()())))(())))))"
lst = "((((((((((()"
curMax = 0
i=0
while i < len(lst):
    if lst[i] == '(':
        balance =0
        length = 0
        j=i
        while j<len(lst):
            if lst[j]=='(':
                balance+=1
            else:
                balance-=1
            if balance<=0:
                if balance == 0:
                    curMax = max(curMax,length+1)
                else:
                    break
            length+=1
            j+=1
        if balance <=0:
            curMax = max(curMax,length)
        i=j
    else:
        i+=1
i=len(lst)-1
while i >=0 :
    if lst[i] == ')':
        balance =0
        length = 0
        j=i
        while j>=0:
            if lst[j]==')':
                balance+=1
            else:
                balance-=1
            if balance<=0:
                if balance == 0:
                    curMax = max(curMax,length+1)
                else:
                    break
            length+=1
            j-=1
        if balance <=0:
            curMax = max(curMax,length)
        i=j
    else:
        i-=1

print(curMax)
