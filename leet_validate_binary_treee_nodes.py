class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        parent = list(range(n))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i,j):
            p1 = find(i)
            p2 = find(j)
            parent[p2] = p1
        
        for i in range(n):
            if left[i] != -1:
                if find(i) == find(left[i]):
                    return False
                union(i,left[i])
            if right[i]!=-1:
                if find(i) == find(right[i]):
                    return False
                union(i,right[i])
        par = find(0)
        for i in range(1,n):
            if find(i) != par:
                return False
        return True