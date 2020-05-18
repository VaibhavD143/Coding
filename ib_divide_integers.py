"""
Gyaan :
XOR operation for 0 1 or 1 0 condition
left shift and right shift use
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        int_max = 2147483647
        int_min = -2147483648
        flag = 1
        if A == 0:
            return 0
        if (A<0) ^ (B<0):
            flag=-1
        A=abs(A)
        B=abs(B)
        res =0
        while A>=B:
            cnt=1
            tmp = B
            while A>(tmp<<1):
                tmp<<=1
                cnt<<=1
            res +=cnt
            A=A-tmp
        res*=flag
        if int_max<res or res<int_min:
            return int_max
        return res