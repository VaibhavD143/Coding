from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts) :
        
        graph = defaultdict(set)
        em_to_nm = {}
        for acc in accounts:
            for email in acc[1:]:
                graph[email].add(acc[1])
                graph[acc[1]].add(email)
            em_to_nm[acc[1]] = acc[0]
        
        
        res = []
        seen = set()
        for email,name in em_to_nm.items():
            if not email in seen:
                ss = [email]
                seen.add(email)
                component = []
                while ss:
                    node = ss.pop()
                    component.append(node)
                    for v in graph[node]:
                        if v not in seen:
                            ss.append(v)
                            seen.add(v)
                res.append([name]+list(sorted(component)))
        return res