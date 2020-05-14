class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, lst):
        i=0
        while i<len(lst):
            if 0<lst[i] <=len(lst):
                # print(i,lst[i])
                # print('in',lst[lst[i]-1])
                if lst[lst[i]-1]==lst[i]:
                    i+=1
                    continue
                lst[lst[i]-1],lst[i]=lst[i],lst[lst[i]-1]
                if i+1 == lst[i]:
                    i+=1
            else:
                i+=1
        for i in range(len(lst)):
            if lst[i]!=i+1:
                return i+1
        return len(lst)+1