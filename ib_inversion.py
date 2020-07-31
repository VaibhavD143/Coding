class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        self.cnt = 0
        self.divide(A)
        return self.cnt
        
    def divide(self,lst):
        if len(lst)<2:
            return lst
        mid = len(lst)//2
        left = self.divide(lst[:mid])
        right = self.divide(lst[mid:])
        
        return self.merge(left,right)
    
    def merge(self,left,right):
        if not left or not right:
            return left or right
        
        res = []
        i1=i2=0
        while i1<len(left) and i2<len(right):
            while i2<len(right) and left[i1]>right[i2]:
                res.append(right[i2])
                i2+=1
            self.cnt+=i2
            res.append(left[i1])
            i1+=1
        while i1<len(left):
            self.cnt+=i2
            res.append(left[i1])
            i1+=1
        while i2<len(right):
            res.append(right[i2])
            i2+=1
        return res
            
        
        