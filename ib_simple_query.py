from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    
    def divisors(self,n):
        self.divs=[1]*(n+1)
        for i in range(2,len(self.divs)):
            for j in range(i,len(self.divs),i):
                self.divs[j]=(self.divs[j]*(i))%1000000007
            
    def solve(self, lst, que):
        self.divisors(max(lst))
        ss=[]
        #ls stores index of element which is grater than that in left side
        ls=[]
        for i,val in enumerate(lst):
            #considering equal as higher as any one side it needs to be considered for case with equal elements
            #BIG CATCH
            while ss and lst[ss[-1]]<val:
                ss.pop()
            if not ss:
                ls.append(-1)
            else:
                ls.append(ss[-1])
            ss.append(i)
        # print(ls)
        ss=[]
        #rs stores element index grater than that in right side
        rs=[]
        for i in range(len(lst)-1,-1,-1):
            #not considering equal as higher as it was considered in left count, for case with equal elements
            while ss and lst[ss[-1]]<=lst[i]:
                ss.pop()
            if not ss:
                rs.append(len(lst))
            else:
                rs.append(ss[-1])
            ss.append(i)
        rs.reverse()
        # print(rs)
        mapp = []
        # print(len(lst))
        # print(lst)
        cnt=0
        for i,val in enumerate(lst):
            cnt+=(rs[i]-i)*(i-ls[i])
            mapp.append([self.divs[val],(rs[i]-i)*(i-ls[i])])
        mapp.sort(reverse=1)
        # print(mapp)
        res = []
        for i in range(1,len(mapp)):
            mapp[i][1]+=mapp[i-1][1]
        pref = list(map(lambda item: item[1],mapp))

        for i in que:
            res.append(mapp[bisect_left(pref,i)][0])
        return res
        # for i in range(len(mapp)):
        #     res+=[mapp[i][0]]*mapp[i][1]
        # # print(res)
        # print(len(res))
        # x =[res[i-1] for i in que]
        # return x