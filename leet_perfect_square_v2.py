import math
class Solution:
    path = [0]
    def numSquares(self, n: int) -> int:
        while len(self.path)<=(n):
            cur = len(self.path)
            for i in range(1,1+int(math.sqrt(len(self.path)))):
                cur =  min(cur,1+self.path[len(self.path)-i*i])
            self.path.append(cur)
        print(self.path)
        return self.path[n]
sol = Solution()
print(sol.numSquares(12))
print(sol.numSquares(17))
print(sol.numSquares(4))
print(sol.numSquares(2))