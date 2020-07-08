class Solution:
    def getProbability(self, balls: List[int]) -> float:
        # @lru_cache(None)
        def rec(ind,n1,n2,rep1,rep2,t1,t2):
            nonlocal sm
            #if ball count in either box exceeds required count `sm` then pruin it
            if t1>sm or t2>sm:
                return 0
            # print(ind,n1,n2)
            #balls list is processed successfully
            if ind == len(balls):
                #if number of unique balls in both bucket is equal and also number of balls
                if n1==n2 and t1 == t2:
                    # print(n1,n2,rep1,rep2,t1,t2)
                    c1=fact[t1]
                    #removing repeating colors ball permutation
                    for i in rep1:
                        c1/=fact[i]
                    c2=fact[t2]
                    #removing repeating colors ball permutation
                    for i in rep2:
                        c2/=fact[i]
                    return c1*c2    #as [1,2/2,3] and [2,1/2,3] is treated different
                return 0
            cnt = 0
            cnt+=rec(ind+1,n1+1,n2,rep1+[balls[ind]],rep2,t1+balls[ind],t2) #assigning all the balls to box1
            cnt+=rec(ind+1,n1,n2+1,rep1,rep2+[balls[ind]],t1,t2+balls[ind]) #assigning all the balls to box2
            #when more than 1 ball exist, then split them, i.e if 3 then (1,2),(2,1). (0,3) and (3,0) has been already processed
            if balls[ind]>1:
                for i in range(1,balls[ind]):
                    cnt+=rec(ind+1,n1+1,n2+1,rep1+[i],rep2+[balls[ind]-i],t1+i,t2+balls[ind]-i)
            return cnt

        sm = sum(balls)//2  #one box will have this many boxes
        fact = [1]
        for i in range(1,50):
            fact.append(fact[-1]*i)
        
        tot = fact[sum(balls)]  #total permutations of all balls
        for i in balls:
            tot/=fact[i]    #removing same color permutations
        
        return rec(0,0,0,[],[],0,0)/tot