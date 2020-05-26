"""
Conditions:
1) Get maximum NUMBER of kicks, strength doesn't matter
2) with minimum lexical order

Intution:
- first get max possible kick by dividing with minimum strength, which is our max number of kicks.
- now we can consider kicks having at lesser indices,
    start from left most index to minimum number index
    - if utilising remaining amount, if length of the result doesn't change then update index
    - repeat till you reach end of result or remaining amount becomes zero or all the considerable numbers exhausted
"""
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        mini = 0
        for ind,val in enumerate(B):
            if val<B[mini]:
                mini = ind
        if A%B[mini] == 0:
            return [mini]*(A//B[mini])
        res = [mini]*(A//B[mini])   #result
        rem = A%B[mini]             #remaining amount
        minVal = B[mini]            #minimum number
        consider = B[:mini]         #considerable numbers for replcement
        ind=0                       #index in result list
        # print(res)
        for i,val in enumerate(consider):
            if rem == 0 or ind ==len(res):
                break
            elif 0<= val-minVal <=rem:
                while 0<= val-minVal<=rem and ind<len(res):
                    res[ind] = i
                    ind+=1
                    rem-= (val-minVal)
        return res
                
        
                
        