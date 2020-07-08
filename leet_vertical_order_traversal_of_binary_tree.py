# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ha = defaultdict(lambda : defaultdict(list))
        ss = [[root,0,0]]
        # low,high=0,0
        while ss:
            node = ss.pop()
            ha[node[1]][node[2]].append(node[0].val)
            # low = min(low,node[1])
            # high = max(high,node[1])
            if node[0].left:
                ss.append([node[0].left,node[1]-1,node[2]+1])
            if node[0].right:
                ss.append([node[0].right,node[1]+1,node[2]+1])
        # res=[[] for _ in range(low,high+1)]
        res = []
        for x in sorted(ha.keys()):
            tres = []
            for y in sorted(ha[x].keys()):
                tres.extend(sorted(ha[x][y]))
            res.append(tres)
        return res