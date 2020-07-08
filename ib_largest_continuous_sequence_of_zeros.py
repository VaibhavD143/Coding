class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        ha= {0:-1}
        prefix=0
        l,r=0,0
        for i,val in enumerate(A):
            prefix += val
            if prefix in ha:
                if i-ha[prefix]>r-l:
                    l=ha[prefix]+1  #ha[prefix] element will be excluded then it will become 0
                    r=i+1   #we are supposed to include current element for sum 0
            else:
                ha[prefix]=i
        return A[l:r]
        