class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        def addStrs(s1,s2):
            if len(s1)>len(s2):
                s1,s2=s2,s1
            carry = 0
            res=""
            for i in range(len(s1)):
                sm = ord(s1[i])+ord(s2[i])-2*ord('0')+carry
                carry=0
                if sm>9:
                    carry=1
                res+=str(sm%10)
            for i in range(len(s1),len(s2)):
                sm = ord(s2[i])-ord('0')+carry
                carry=0
                if sm>9:
                    carry=1
                res+=str(sm%10)
            res+='1'if carry else ''
            return res
        
        res="0"
        A=A[::-1]
        B=B[::-1]
        for i in range(len(B)):
            tres = "0"
            for _ in range(ord(B[i])-ord('0')):
                tres = addStrs(tres,A)
            res = addStrs(res,"0"*i+tres)
            
        return res[::-1].lstrip('0') if res[::-1].lstrip('0') else "0"