from collections import Counter

s = "GEEKSGEEKSFOR"
s = "AABBBCBBAC"
s = "AABBBCBB"
s = "aabcbcdbca"
s= "aaab"
chars = set(s)
cnt = Counter()
diff = len(chars)
l = 0
res = len(s)

for r in range(len(s)):
    cnt[s[r]]+=1
    if cnt[s[r]] == 1:
        diff-=1
    while diff == 0:
        if res>r-l+1:
            print(s[l:r+1])
        res = min(res,r-l+1)
        cnt[s[l]]-=1
        if cnt[s[l]] == 0:
            diff+=1
        l+=1
print(res)
s1 = "abcdef"
s2 = "e-fabcde"
d = len(s)
chars = 256
q = 10**9+7

a,b,c
hash(s1) = (a*d^2+b*d+c)%q
i = 0
hs20 = hash(s2)
i=1
hs21 = chars(hs20 - (chars^d-1))+ord('e')
