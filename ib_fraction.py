"""
Gyaan:
Use Xor condition for 1 0 or 0 1 case!
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        if A == 0:
            return "0"
        #lef part of decimal
        left=''
        #Any one is negative then nagative sign
        if (A<0)^(B<0):
            left='-'
        #Doing division manually
        A=abs(A)
        B=abs(B)
        left+=str(A//B)
        rem = A%B
        if rem == 0:
            return left
        right=''
        #To store rem, if remainder repeats, then patter from there repeats
        ha = {}
        #to know from which index in 'right' pattern starts repeating
        cnt=0
        # print(rem,rem*10,(rem*10)/B,(rem*10)//B)
        while rem:
            ha[rem]=cnt
            right += str((rem*10)//B)
            rem = (rem*10)%B
            if rem in ha:
                break
            cnt+=1
        if rem :
            return left+'.'+right[:ha[rem]]+'('+right[ha[rem]:]+')'
        return left+'.'+right