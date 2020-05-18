class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        if len(A) == 1 or A == '0':
            return 1
        prefix = [1]
        for i in A:
            if i =='0':
                return 0
            prefix.append(int(i)*max(prefix[-1],1))
        ha = {}
        # prefix[0]=0
        for i in range(1,len(A)+1):
            for j in range(len(A)-i+1):
                res = prefix[j+i]//prefix[j]
                if res in ha:
                    return 0
                ha[res]=1
        return 1