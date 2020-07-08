class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # rows = [[min(r),r.index(min(r))] for i,r in enumerate(matrix)]
        # cols = [max(item[i] for item in matrix) for i in range(len(matrix[0]))]
        # for r in rows:
        #     if r[0] == cols[r[1]]:
        #         yield r[0]
        return list({min(r) for r in matrix}&{max(c) for c in zip(*matrix)})