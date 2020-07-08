class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         ch = "abc"
#         cnt = [0,0,0]
#         l,r = 0,0
#         res=0
#         last = -1
#         while r<len(s):
#             cnt[ch.index(s[r])]+=1
#             # print(cnt,r,cnt[0]&cnt[1]&cnt[2])
#             if cnt[0] and cnt[1] and cnt[2]:
#                 while True:
#                     cnt[ch.index(s[l])]-=1
#                     if cnt[ch.index(s[l])] == 0:
#                         break
#                     l+=1
#                 left = l-last
#                 right = len(s)-r
                
#                 res+=(left*right)
#                 last= l
#                 l+=1
#             r+=1
#         return res
    def numberOfSubstrings(self, s):
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in range(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res