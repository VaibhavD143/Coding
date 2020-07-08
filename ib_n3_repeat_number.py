"""
Intution:
whene we encounter 3 unique elements, we can discard them from the list and our answer won't change at all
so we keep K-1 size array to keep count of elements

if it exist in list then increament count
if doesn't exist and we have't found K-1 elements then add it
if this is unique element then remove pair of these elements by decreasing count by 1,
    if count falls to 0 then that element is no more candidate for solution

count for candidate elements

"""

from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        cnt = [0]*2
        buck = [None]*2
        def addItem(n):
            for i in range(len(cnt)):
                if buck[i] == n:
                    cnt[i]+=1
                    return
            
            for i in range(len(cnt)):
                if buck[i] == None:
                    buck[i]=n
                    cnt[i]=1
                    return
            for i in range(len(cnt)):
                cnt[i]-=1
                if cnt[i]<1:
                    buck[i]=None
                    cnt[i]=0
        # print(len(A)/3.0)
        # print(Counter(A))
        for i in A:
            addItem(i)
        # print(5/3.0)
        # print(buck)
        for cand in buck:
            cnt=A.count(cand)
            if cnt>len(A)/3.0:
                return cand
        
        return -1
            
        