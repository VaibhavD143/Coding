from itertools import combinations_with_replacement
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, digs, rem, lim):
        def find(num,rem,digs,lim):
            # print(num if num<lim else -1)
            if rem==0 :
                return 1 if num<lim else 0 #because less than number not <= i.e for lim = 561, to avoid 561
            cnt=0
            res=0
            for dig in digs:
                if num+dig <lim[:len(num)+1]:
                    cnt+=1  #when all the remaining places can be filled with permutations, cnt is count of possible dig for current place which generate lesser num for sure. so rest places can be any digits
                elif num+dig == lim[:len(num)+1]:
                    res+=find(num+dig,rem-1,digs,lim) #when current position generates exact value i.e. lim =561, currentl generated num is 56
                    break
                else:
                    break
            res = res + cnt*(len(digs)**(rem-1))
            return res
        res=0
        if rem ==1:
            #case where only '0' is the answer
            for i in digs:
                res+=1 if i<lim else 0
            return res
        lim = str(lim)
        if rem>len(lim) or len(digs) ==0:
            #not possible case
            return 0
        # print(digs)
        if rem < len(lim):
            # when required length is lesser than lim length
            #all permutations
            if 0 in digs:
                #0 can't be first digit so ignore if exist
                return (len(digs)-1)*(len(digs)**(rem-1))
            return len(digs)**rem
        digs = list(map(str,digs))
        digs.sort()
        for dig in digs:
            if dig != '0' and dig <= lim[0]:
                res+=find(dig,rem-1,digs,lim)
        return res