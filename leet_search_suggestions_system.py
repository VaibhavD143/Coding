class Solution:
    def suggestedProducts(self, pro: List[str], sw: str) -> List[List[str]]:
        pro.sort()
        ha = {}
        res = []
        lst = range(len(pro))
        for i in range(len(sw)):
            tres = []
            tlst = []
            for j in lst:
                if len(pro[j])>i and pro[j][i] == sw[i]:
                    tlst.append(j)
            for j in range(min(3,len(tlst))):
                tres.append(pro[tlst[j]])
            res.append(tres)
            lst = tlst
        return res    