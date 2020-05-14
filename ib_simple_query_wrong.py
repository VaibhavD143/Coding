from bisect import *
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def __init__(self):
        self.divs=[1]*(100002)
        self.divisors()
    
    def divisors(self):
        for i in range(2,100001//2):
            for j in range(i,100002,i):
                self.divs[j]=(self.divs[j]*(i))%1000000007
            
    def solve(self, lst, que):
        ss=[]
        ls=[]
        for i,val in enumerate(lst):
            while ss and lst[ss[-1]]<val:
                ss.pop()
            if not ss:
                ls.append(-1)
            else:
                ls.append(ss[-1])
            ss.append(i)
        print(ls)
        ss=[]
        rs=[]
        for i in range(len(lst)-1,-1,-1):
            while ss and lst[ss[-1]]<=lst[i]:
                ss.pop()
            if not ss:
                rs.append(len(lst))
            else:
                rs.append(ss[-1])
            ss.append(i)
        rs.reverse()
        print(rs)
        mapp = []
        print(len(lst))
        print(lst)
        cnt=0
        for i,val in enumerate(lst):
            cnt+=(rs[i]-i)*(i-ls[i])
            mapp.append([self.divs[val],(rs[i]-i)*(i-ls[i])])
        mapp.sort(reverse=1)
        print(mapp)
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
            
obj = Solution()
# print(obj.solve([39, 99, 70, 24, 49, 13, 86, 43, 88, 74, 45, 92, 72, 71, 90, 32, 19, 76, 84, 46, 63, 15, 87, 1, 39, 58, 17, 65, 99, 43, 83, 29, 64, 67, 100, 14, 17, 100, 81, 26, 45, 40, 95, 94, 86, 2, 89, 57, 52, 91, 45 ],[1,5, 20, 25, 30, 35, 40, 45, 50, 55]))
# print(obj.solve([],[1,5, 20, 25, 30, 35, 40, 45, 50, 55]))
print(obj.solve([1,2,4],[1,2,3,4,5,6]))
#100 100 36 27 27 8 7 5 3 1
#1 5 20 25 30 35 40 45 50 100