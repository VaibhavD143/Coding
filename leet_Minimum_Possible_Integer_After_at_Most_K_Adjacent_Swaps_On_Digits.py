class Solution:
    def minInteger(self, num: str, k: int) -> str:
        def update(ind,bit):
            ind=ind+1
            while ind<len(bit):
                bit[ind]+=1
                ind += (ind&-ind)
        
        def getSum(ind,bit):
            ind+=1
            res=0
            while ind>0:
                res+=bit[ind]
                ind-=(ind&-ind)
            return res
        
        bit = [0]*(1+len(num))
        
        ind = {i:deque([]) for i in range(10)}
        for i,n in enumerate(num):
            ind[int(n)].append(i)
        res = []
        for i in range(len(num)):
            for dig in range(10):
                if ind[dig]:
                    pos = ind[dig][0]
                    dist = pos-getSum(pos,bit)
                    if dist<=k:
                        k-=dist
                        res.append(str(dig))
                        ind[dig].popleft()
                        update(pos,bit)
                        break
                        
        return ''.join(res)