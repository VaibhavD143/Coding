    
class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = [0]*(n+1)
        for i in range(1,n+1):
            sm = 0
            while i:
                sm+=i%10
                i//=10
            cnt[sm]+=1
        return cnt.count(max(cnt))

    def countLargestGroup2(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            counts[dp[i] - 1] += 1

        return counts.count(max(counts))