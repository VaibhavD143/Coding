"""
https://leetcode.com/problems/largest-number/solution/
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1,s2):
            n1 = int(''.join(s1+s2))
            n2 = int(''.join(s2+s1))
            return n2-n1
        def cmp_to_key(compare):
            'Convert a cmp= function into a key= function'
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return compare(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return compare(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return compare(self.obj, other.obj) == 0
                def __le__(self, other):
                    return compare(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return compare(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return compare(self.obj, other.obj) != 0
            return K

        lst = map(str,nums)
        lst = sorted(lst,key = cmp_to_key(compare))
        res = ''.join(lst)
        return res if res[0] =='0' else '0'