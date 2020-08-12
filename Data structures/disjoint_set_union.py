"""
Disjoint Union algo with and without Union-by-rank
https://leetcode.com/articles/redundant-connection/
"""

def union(i1,i2):
    p1 = find(i1)
    p2 = find(i2)
    
    if p1 == p2:
        return
    if rank[p1]>rank[p2]:
        p1,p2 = p2,p1
    
    parent[p1] = p2
    rank[p2]+=1

def find(i1):
    if parent[i1] != i1:
        parent[i1] = find(parent[i1])
    return parent[i1]

parent = list(range(len(A)))
rank = [0]*len(A)

class DSUwithputRank:
    def __init__(self):
        self.par = list(range(1001))
    def find(self, x):
        # if not leader then do update
        if self.par[x] != x:
            # path compression : so it will start directly pointing to actual leader of set and next time will require lesser jumps
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        # setting leader of Y as parent of leader of X, so now X and Y set will both belong to same set
        self.par[self.find(x)] = self.find(y)

class DSU(object):
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        # union-by-rank algo to optimise the jumps, selecting leader with higher followers to have new followe so lesser umber of followes have to
        # make that new jump
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
