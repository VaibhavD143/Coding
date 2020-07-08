"""
Intution:
ha[start,end] : stores cost of cutting rod from start and end, where start and end are exclusive, for rod length. They are not part of cuts
path[start,end] : stores first cut will be made for rod index [start,end]

"""
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        
        def rec(start,end):
            if end-start==2:
                path[start,end] = start+1
                return B[end]-B[start]
            if end-start<2:
                return 0
                
            if (start,end) in ha:
                return ha[start,end]
            
            c = float('inf')
            for i in range(start+1,end):
                tcost1= rec(start,i)
                tcost2 = rec(i,end)
                if tcost1+tcost2<c:
                    c = tcost1+tcost2
                    path[start,end] = i
            ha[start,end] = c+B[end]-B[start]
            return ha[start,end]
        if len(B)<2:
            return B
        path={}
        ha={}
        B = [0]+B+[A]
        rec(0,len(B)-1)
        res = []
        ss=[[0,len(B)-1]]
        while ss:
            l,r=ss.pop()
            if r-l == 2:
                res.append(B[path[l,r]])
                continue
            if r-l<2:
                continue
            k=path[l,r]
            res.append(B[k])
            ss.append([k,r])
            ss.append([l,k])
        return res