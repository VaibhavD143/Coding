"""
Intution:
Binart search on length of substring
to check if such length duplicate substring is possible we are using rolling hash (Rabin karp's algortihm)
n = length of substring we are looking for = 3
d = number of character possible in string = 256 ASCII
q = big prime number to reduce the size into smaller value
h = biggest multiplication to character, multiplier of fisrt character = pow(d,n-1,q) = d^2
`h` is precomputed as we will be using it a lot
t = hash of text
s = "abcd"
t0 = hash("abc") = (ord('a')*d^2+ord('b')*d^1+ord('c')*d^0)%q
t1 = hash("bcd") = (d*(t0-ord('a')*h)+ord('d'))%q
removing 'a' contribution, promoting each character by multiplying with `d` and adding contribution of `d`
"""
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def isPossible(n):
            if n == 0:
                return 0,0
            q = 2**31-1
            d = 256 #number of characters
            t=0
            h = pow(d,n-1,q)
            p=0
            for i in range(n):
                t=(d*t+ord(s[i]))%q
            ha = {t:[0]}
            for i in range(1,len(s)-n+1):
                t = (d*(t-(ord(s[i-1])*h))+ord(s[i+n-1]))%q
                if t in ha:
                    for j in ha[t]:
                        if s[j:j+n] == s[i:i+n]:
                            return j,j+n
                    ha[t].append(i)
                else:
                    ha[t] = [i]
            return False,False
        lo,hi = 0,len(s)-1
        res=""
        while lo<=hi:
            mid = lo+(hi-lo)//2
            ss,se = isPossible(mid)
            if ss ==False and se == False:
                hi=mid-1
            else:
                res = s[ss:se]
                lo = mid+1
        return res