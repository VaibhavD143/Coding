v1 = "7.0.1"
v2 = "7"
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
    
        l1 = list(map(int,v1.split(".")))
        l2 = list(map(int,v2.split(".")))
        #1.0.0 and 1.0
        while l1 and l1[-1] == 0:
            l1.pop()
        while l2 and l2[-1] == 0:
            l2.pop()
        # print(l1,l2)
        return 1 if l1>l2 else -1 if l1<l2 else 0