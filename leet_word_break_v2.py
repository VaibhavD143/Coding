s = "leetcode"
s = "applespenapple"
s = "catsandog"
wordDict = ["leet", "code"]
wordDict = ["apple","apples", "pen"]
wordDict = ["cats", "dog", "sand", "and", "cat"]
s="a"
wordDict = ["a"]
ok = [0]*(len(s))
for i in range(len(s)):
    for word in wordDict:
        if len(word) <= i+1 and (i-len(word)==-1 or ok[i-len(word)]) and s[i-len(word)+1:i+1] == word:
            ok[i] = 1
            break



print(ok)



# for i in range(1,1+len(s)):
#     for word in wordDict:
#         # print(i+1>=len(word) , ok[i-len(word)+1] , s[i-len(word)+1:i+1] == word,i,i-len(word)+1,s[i-len(word)+1:i+1],word)
#         if i+1>=len(word) and ok[i-len(word)+1] and s[i-len(word)+1:i+1] == word:
#             ok[i+1] = 1
#             break