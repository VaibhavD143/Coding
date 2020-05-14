string = "mississippi"
pat = "mis*is*p*."
string = "aab"
pat = "c*a*b"
string = "azbvzaabb"
pat = "z.*"
string = ""
pat= "za*b*c*"
string = list(string)
string.reverse()
tpat = []
i = len(pat)-1
while i >=0:
    if pat[i] == '*':
        tpat.append('*'+pat[i-1])
        i-=1
    else:
        tpat.append(pat[i])
    i-=1
if len(string) == 0 and len(tpat) ==0:
    print(True)
    exit(1)
if len(tpat) == 0:
    print(False)
    exit(1)

dp = [[0]*(len(string)+1) for _ in range(1+len(tpat))]
dp[0][0] = 1
print(string)
print(tpat)
for i in range(1,len(tpat)+1):

    if tpat[i-1] == '.':
        #mark yes if excluding this regx and current character it was True
        for j in range(1,len(string)+1):
            dp[i][j] = dp[i-1][j-1]
    elif tpat[i-1][0] != '*':
        #if it is just normal character, mark yes if it matches with current string character and excluding this regx and character it was True
        for j in range(1,len(string)+1):
            if tpat[i-1] == string[j-1] and dp[i-1][j-1]:
                dp[i][j]=1
    else:
        if tpat[i-1][1] == '.':
            """
            when regx is of type "*.", accept when True without regx(dp[i-1][j-1]), when True till previos string character(dp[i][j-1]),
            when it was True including current character as zero or more(dp[i-1][j])
            """
            dp[i][0] = dp[i-1][0]
            for j in range(1,len(string)+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        else:
            """
            when regx is of type "*b,*q", accept if True with current inclusion(dp[i-1][j]) as zero or more,
            when regx character matches with current string character 
            AND 
            it was True till previous character includinf regx or it was True exluding regx & string character
            """
            dp[i][0] = dp[i-1][0]
            for j in range(1,len(string)+1):
                if dp[i-1][j] or (string[j-1] == tpat[i-1][1] and (dp[i-1][j-1] or dp[i][j-1])): 
                    dp[i][j] = 1

for i in dp:
    print(i)