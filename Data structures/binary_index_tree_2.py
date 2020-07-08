class BITsum:
    def updateSum(self,bit,ind,val):
        ind+=1
        while ind<len(bit):
            bit[ind]+=val
            ind+=ind&(-ind)
        
    def getSum(self,bit,ind):
        ind+=1
        res=0
        while ind>0:
            res+=bit[ind]
            ind-=ind&(-ind)
        return res

    def construct_sum(self,arr):
        bit = [0]*(len(arr)+1)

        for i,val in enumerate(arr):
            self.updateSum(bit,i,val)
        return bit

class BITmax:
    def updateMax(self,bit,ind,val):
        ind +=1
        while ind<len(bit):
            if bit[ind]>val:
                break
            bit[ind] = val
            ind += (ind&-ind)
        
    def getMax(self,bit,ind):
        ind+=1
        res = 0
        while ind>0:
            res = max(res,bit[ind])
            ind-=(ind&-ind)
        return res
    
    def construct_max(self,arr):
        bit = [float('-inf')]*(1+len(arr))

        for i,val in enumerate(arr):
            self.updateMax(bit,i,val)
        return bit