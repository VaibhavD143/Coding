""""
mask : ith bit represents presence of ith skill from req_skills
allone : all skills are present
s2p : skill to people mapping
s2i : skill to index mapping
dp[mask,len] : with len of people and skills mask is processed so don't process further as we won't get any BETTER result
lst : current team of people
"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        s2p = {skill : [] for skill in req_skills}
        s2i = {skill : ind for ind,skill in enumerate(req_skills)}
        
        for ind,p in enumerate(people):
            for sk in p:
                s2p[sk].append(ind)
        
        allone = (1<<len(req_skills))-1
        mask = 0
        dp = set()
        
        def rec(mask,i):
            # print(mask,i,lst)
            nonlocal res
            if mask == allone:
                
                if len(lst)<len(res):
                    res = lst[:]
                return False
            
            if len(res)<=len(lst):
                dp.add((mask,len(lst)))
                return False
            
            if (mask,len(lst)) in dp:
                return False
            if mask&(1<<i):
                return rec(mask,i+1)
            
            for p in s2p[req_skills[i]]:
                lst.append(p)
                tmask = mask
                for s in people[p]:
                    tmask|=(1<<s2i[s])
                rec(tmask,i+1)
                lst.pop()
            dp.add((mask,len(lst)))
            return False
        lst = []
        res = list(range(len(people)))
        # print(s2i)
        # print(s2p)
        rec(0,0)
        return res