from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def rec(s1,s2):
        
            if Counter(s1) != Counter(s2):
                return False
            if s1 == s2:
                return True
            
            if (s1,s2) in ha:
                return ha[(s1,s2)]
            
            for i in range(1,len(s1)):
                if rec(s1[:i],s2[:i]) and rec(s1[i:],s2[i:]):
                    ha[(s1,s2)] = True
                    return True
                if rec(s1[-i:],s2[:i]) and rec(s1[:-i],s2[i:]):
                    ha[(s1,s2)] = True
                    return True
                
            ha[(s1,s2)] = False
            return False
            
        if not s1 and not s2:
            return False
        
        ha={}
        return 1 if rec(s1,s2) else 0
        
        def rec2(s1,s2):
            # print(s1,s2)
            if not s1 or not s2:
                return False
            if s1 == s2:
                ha[(s1,s2)] =True
                return True
            if (s1,s2) in ha:
                return ha[(s1,s2)]
            cnt1 = Counter()
            cnt2 = Counter()
            cnt1_b = Counter()
            
            for i in range(len(s1)-1):
                cnt1[s1[i]]+=1
                cnt1_b[s1[len(s1)-i-1]]+=1
                cnt2[s2[i]]+=1
                # print(s1,s2,i,cnt1,cnt1_b,cnt2)
                if cnt2 == cnt1 and rec(s1[:i+1],s2[:i+1]) and rec(s1[i+1:],s2[i+1:]):
                    ha[(s1,s2)] = True
                    return True
                if cnt2 == cnt1_b and rec(s1[::-1][:i+1],s2[:i+1]) and rec(s1[::-1][i+1:],s2[i+1:]):
                    ha[(s1,s2)] = True
                    return True
            ha[(s1,s2)] = False
            return False
            
            
        
        if Counter(s1) != Counter(s2):
            return 0
        ha={}
        # rec(0,len(A)-1)
        # print(ha)
        return 1 if rec2(s1,s2) else 0
             