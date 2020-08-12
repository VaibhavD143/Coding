A = ["adc", "aec", "erg"]
target = "ac"
A = ["afsdc", "aeeeedc", "ddegerg"]
target = "ae"
# (indexOfWord,indexOfCharINWOrd,IndexOfCharInTarget)
# def findWays()

# (indW,indA,indT)
# (0,0,0):
#     - (1,0,1)
#     - (0,1,0)
# (0,0,0):
#     - (1,0,0)
#     - (0,1,0)

# wordLen = len(A[0])

# if indT = len(target):
#     return 1
# if indA>=len(A):
#     return 0
# if indW>=len(wordLen):
#     return 0

def findWays(indW,indT):
    if indT == len(target):
        return 1
    if indW == len(A[0]):
        return 0
    if len(target)-indT>len(A[0])-indW:
        return 0

    if (indW,indT) in dp:
        return dp[indW,indT]
    
    cnt = 0
    cnt+=findWays(indW+1,indT)
    for i in range(len(A)):
        if A[i][indW] == target[indT]:
            cnt+=findWays(indW+1,indT+1)
    dp[indW,indT] = cnt
    return cnt

dp ={}
print(findWays(0,0))
