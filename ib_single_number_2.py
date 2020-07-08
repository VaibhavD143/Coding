"""
Intution:
for any bit position it can occure for 3x+1 times,
if 0 doesn't matter
if 1 then it should stay 1
so,
When hits 1st time, keeping record in ones
when second time, keeping it in twos
and on 3rd time clearing it from them

so left ones is the answer
"""
import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for i in A:
            for j in range(32):
                if i&(1<<j):
                    if ones&(1<<j):
                        if twos&(1<<j):
                            twos = twos^(1<<j)
                            ones = ones^(1<<j)
                        else:
                            twos = twos|(1<<j)
                    else:
                        ones = ones|(1<<j)
                        # print(ones)
        return ones
    def singleNumber2(self, A):
        
        #Complexity of this solution is O(32*N) = O(N)
        
        # Assumging 32 bit integer
        INT_SIZE = 32
        
        result = 0
        
        # Iterate for every bit position
        for i in range(0,INT_SIZE):
            
            sm = 0
            
            # Used to check if ith bit is 1 or not.
            x = (1<<i)
            
            for j in range(0,len(A)):
                
                # This will only be true, if ith bit is set (=1)
                if(A[j]&x):
                    sm = sm+1
                    
            # Set ith bit  of result based on whether the ith bit occured 3 times or not.
            # Only the bits that occured 1 time will be 1
            if (sm % 3) :
                result = result | x
                
        return result