#https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/discuss/609678/Python-O(k-*-logk-*-len(mat))-with-detailed-explanations-%2B-4-lines-python.
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        dp = mat[0][:]
        for row in mat[1:]:
            dp = sorted([i+j for i in row for j in dp])[:k]
        return dp[k-1]