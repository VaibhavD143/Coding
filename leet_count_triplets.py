"""
Editorial by `lee215`
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr)<2:
            return 0
        pref =[0]
        for i in arr:
            pref.append(pref[-1]^i)
        # print(pref)
        res=0
        for i in range(1+len(arr)):
            for j in range(i+1,1+len(arr)):
                if pref[i]==pref[j]:
                    res+=(j-i-1)
        return res