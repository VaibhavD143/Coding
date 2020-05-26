"""
Intution:
Greates divisior of A is A itself, now to make it co-prime with B, we remove common factors from it.
When there is no common factor left. It is the answer!
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
    
        def gcd(q1,q2):
            #q1>=q2
            if q1%q2 == 0:
                return q2
            return gcd(q2,q1%q2)
        if B==0:
            return A
        while True:
            com = gcd(max(A,B),min(A,B))
            if com == 1:
                return A
            A = A//com