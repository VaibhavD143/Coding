"""
gfg too
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        l=0
        r=len(A)-1
        l_elm = A[0]
        while l<=r:
            mid = (l+r)//2
            
            if B==A[mid]:
                return mid
            # print(l,mid,r)
            if A[l] < A[mid]: 
                if A[l] <= B <A[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if A[mid] < B <=A[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

def binary_search(lst,elm):
	f = 0
	r = len(lst)
	pmid = -1
	mid = (f+r) //2

	while f != r:
		if lst[mid] == elm:
			return mid
		elif lst[mid] > elm:
			r = mid
		else:
			f = mid+1
		
		pmid = mid
		mid = (f+r) //2
	# return mid #to return index of next present number
	return -1 #to return -1 if not present

for _ in range(1):
# for _ in range(int(input())):
    # n = int(input())
    lst = [4,5,6,7,0,1,2]
    # lst = list(map(int,input().split()))
    n = len(lst)
    k = 0
    # k = int(input())
    i = 0
    j = n-1
    elem = lst[0]
    while i<j:
        mid = (i+j)//2
        if lst[mid]>=elem:
            i=mid+1
        else:
            j=mid-1
    if lst[i] >= elem:
        part = (i+1)
    else:
        part = i
    
    if k>=lst[0]:
        ind = binary_search(lst[:part],k)
    else:
        ind = binary_search(lst[part:],k)
        if ind !=-1:
            ind+=part
    print(ind)