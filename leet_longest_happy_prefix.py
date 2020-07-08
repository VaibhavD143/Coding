class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0]
        i=1
        l = 0
        while i<len(s):
            if s[l] == s[i]:
                l+=1
                lps.append(l)
                i+=1
            else:
                if l!=0:
                    l=lps[l-1]
                else:
                    lps.append(0)
                    i+=1
        return s[-lps[-1]:] if lps[-1] != 0 else ""