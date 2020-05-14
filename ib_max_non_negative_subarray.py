class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, lst):
        if not lst:
            return 0
        res = lst[0]
        curr= lst[0]
        l=0
        r=0
        curr_l=0 if lst[0]>=0 else 1 #it stores left most index of current sum, if current sum is negative then next index of it
        for i in range(1,len(lst)):
            if lst[i]>=0:
                curr=max(0,curr)    #if it was negative before and array sum starting from here
                curr+=lst[i]
                if res <=curr:
                    if res == curr:
                        if(r-l)<(i-curr_l): #when tie in sum go for longer length and '<' without equal because tie in length then lower index
                            l=curr_l
                            r=i
                    else:
                        res=curr
                        l=curr_l
                        r=i
            else:
                curr=lst[i]
                curr_l=i+1
        return lst[l:r+1] if res>=0 else [] #when all are negative then return []