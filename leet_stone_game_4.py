class Solution:
    # self.root = []
    # def generate(self,n):
    #     if len(self.root)<n:
    #         while 
    def winnerSquareGame(self, n: int) -> bool:
        
        
#         def rec(n):
#             # print(n,flag)
#             if n == 0:
#                 return False

#             if dp[n]!= None:
#                 return dp[n]
            
#             sq = int(n**0.5)
#             dp[n] = False
#             for i in range(1,sq+1):
#                 res = rec(n-i**2)
#                 if not res:
#                     dp[n] = True
#                     break
            
#             return dp[n]
#         return rec(n)
        dp = [False]*(n+1)
        sq = []
        for i in range(1,int(n**0.5)+1):
            sq.append(i*i)
        # print(sq)
        for i in range(1,n+1):
            for num in sq:
                if num>i:
                    break
                if dp[i-num] == False:
                    dp[i] = True
                    break
        return dp[-1]