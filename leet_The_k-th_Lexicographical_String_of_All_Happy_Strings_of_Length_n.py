class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr = ['a','b','c']
        tot = 3*(2**(n-1))
        if k>tot:
            return ""
        k-=1
        res=""
        while n:
            skip = 2**(n-1)
            ind = k//skip
            res+=curr[ind]
            k-=ind*skip
            curr = ['a','b','c']
            curr.remove(res[-1])
            n-=1
        return res
    def getHappyString2(self, n: int, k: int) -> str:
        k -= 1
        if k // 2 ** (n - 1) > 2: return ''
        result, lookup = '^', {'^': 'abc', 'a': 'bc', 'b': 'ac', 'c': 'ab'}
        for i in reversed(range(n)):
            idx, k = divmod(k, 2 ** i)
            result += lookup[result[-1]][idx]
        return result[1:]