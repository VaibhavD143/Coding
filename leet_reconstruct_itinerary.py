"""
Intution:
Version-1:
Generate all possible paths from current vertex, and if multiple paths are possible then merge them into one
HOW?
as vertices are sorted, paths are already in sorted order.
there will be only one path which is not reaching back to start vertex, rest will form a cycle
Append that path in the last as it is going out of vertex and not returning back
Version 2:
euclrean path algo
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ha={}
        for t in tickets:
            if t[0] not in ha:
                ha[t[0]]=[t[1]]
            else:
                ha[t[0]].append(t[1])
        for k in ha:
            ha[k].sort(reverse=True)
        # def rec(start):
        #     if start not in ha or not ha[start]:
        #         return [[start]]
        #     res=[]
        #     # l=len(ha[start])
        #     while ha[start]:
        #         res.extend([start]+r for r in rec(ha[start].pop()))
        #     path = [start]
        #     last = None
        #     for r in res:
        #         if r[-1]!=start:
        #             last = r
        #         else:
        #             path.extend(r[1:])
        #     if last:
        #         path.extend(last[1:])
        #     return [path]
        # return rec("JFK")[0]
        res=[]
        def dfs(key):
            if key in ha:
                while ha[key]:
                    dfs(ha[key].pop())
            res.append(key)
        dfs("JFK")
        return res[::-1]