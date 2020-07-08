class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l=[0]*len(rating)
        r=[0]*len(rating)
        for i in range(len(rating)):
            for j in range(i-1,-1,-1):
                if rating[j]>rating[i]:
                    l[i]+=1
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    r[i]+=1
        # print(l)
        # print(r)
        res=0
        for i in range(len(rating)):
            for j in range(i-1,-1,-1):
                if rating[j]>rating[i]:
                    res+=l[j]
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    res+=r[j]
        return res        