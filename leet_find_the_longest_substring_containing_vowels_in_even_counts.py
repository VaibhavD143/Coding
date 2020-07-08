"""
Intution:
Each bit represents a presence of vowel,
if bit is 0 then vowel is present even times
if bit is 1 then vowel is present odd times
we keep track of mask from the begining storing left most occurrence
and whenever we get same same mask in, it is length
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        vowels = 'aeiou'
        ha = {0:-1}
        res = 0
        for i,ch in enumerate(s):
            if ch in vowels:
                mask^=(1<<vowels.index(ch))
            if mask in ha:
                res = max(res,i-ha[mask])
            else:
                ha[mask] = i
        return res