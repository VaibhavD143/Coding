class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ha ={}
        res = []
        for name in names:
            if name not in ha:
                res.append(name)
                ha[name] = 1
            else:
                n = ha[name]
                # print(name,n)
                while True:
                    s = name+'('+str(n)+')'
                    if s not in ha:
                        res.append(s)
                        ha[name]=n+1
                        ha[s]=1 #if same name occures in next iteration
                        break
                    n+=1
        return res