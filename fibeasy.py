"""
https://www.codechef.com/SEPT19B/problems/FIBEASY
"""

import math
def fib(n): 
      
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
          
    return F[0][0] 
      
def multiply(F, M): 
      
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] + 
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x%10 
    F[0][1] = y%10
    F[1][0] = z%10 
    F[1][1] = w%10 
          
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 
    M = [[1, 1], 
         [1, 0]]; 
          
    power(F, n // 2) 
    multiply(F, F) 
          
    if (n % 2 != 0): 
        multiply(F, M) 
      
# Driver Code 
if __name__ == "__main__": 
    
    for _ in range(int(input())):
        n = int(input())
        lno = math.floor(math.log2(n))
        n = 2**lno

        print(fib(n-1)%10)