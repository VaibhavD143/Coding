class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        if len(A)>len(B):
            A,B=B,A
        A=A[::-1]
        B=B[::-1]
        res=""
        carry = 0
        for i in range(len(A)):
            sm = int(A[i])+int(B[i])+carry
            carry=0
            if sm==0:
                res+='0'
            elif sm==1:
                res+='1'
            elif sm==2:
                res+='0'
                carry =1
            elif sm==3:
                res+='1'
                carry=1
        for j in range(len(A),len(B)):
            sm =int(B[j])+carry
            carry=0
            if sm==0:
                res+='0'
            elif sm==1:
                res+='1'
            elif sm==2:
                res+='0'
                carry =1
            elif sm==3:
                res+='1'
                carry=1
        res+="1" if carry else ""   #last carry
        return res[::-1].lstrip('0') if res[::-1].lstrip('0') else "0" #when answer is zero