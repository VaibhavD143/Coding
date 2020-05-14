"""
Given a string str, the task is to find the minimum number of characters to be inserted to convert it to palindrome
https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
"""

string = "abcda"
l_str = len(string)
dp = [[-1]*l_str for i in range(l_str)]

def minInsertion(string,l,h):
    global dp
    if l >= h:
        return 0
    else:
        if string[l] == string[h]:
            if dp[l+1][h-1] == -1:
                dp[l+1][h-1] = minInsertion(string,l+1,h-1)
            return dp[l+1][h-1]
        else:
            if dp[l+1][h] == -1:
                dp[l+1][h] = minInsertion(string,l+1,h)
            if dp[l][h-1] == -1:
                dp[l][h-1] = minInsertion(string,l,h-1)
            return min(dp[l+1][h],dp[l][h-1])+1

print(minInsertion(string,0,l_str-1))