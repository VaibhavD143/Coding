"""
count displacement from actual position of character from current set
"""
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if len(A)<2:
            return 1
        srtd = sorted(A)
        rank = 0
        fact = [1,1]
        for i in range(2,len(A)):
            fact.append((fact[-1]*i)%1000003)
            
        for i,ch in enumerate(A):
            ind = srtd.index(ch)
            srtd.remove(ch)
            rank+= (ind*fact[len(A)-i-1])
        return (rank+1)%1000003