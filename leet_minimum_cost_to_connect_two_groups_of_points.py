"""
intution:
fill up all the nodes from set1 and then fill remainning from set2
m1 is for set1 and set bit represents node is connected
m2 is for set2
"""
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        fm1 = (1<<len(cost))-1
        fm2 = (1<<len(cost[0]))-1
        def fun(m1,m2):
            if m1==fm1 and m2 == fm2:
                return 0
            
            if (m1,m2) in ha:
                return ha[m1,m2]
            
            cst = float('inf')
            if m1!=fm1:
                for i in range(len(cost)):
                    if m1&(1<<i) == 0:
                        for j,val in enumerate(cost[i]):
                            cst = min(cst,fun(m1|(1<<i),m2|(1<<j))+cost[i][j])
                        break
            else:
                for j in range(len(cost[0])):
                    if m2&(1<<j) ==0:
                        for i in range(len(cost)):
                            cst = min(cst,fun(m1|1<<i,m2|1<<j)+cost[i][j])
                        break
            ha[m1,m2] = cst
            return cst
        
        ha={}
        return fun(0,0)