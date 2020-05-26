class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return all(x<=y for x,y in zip(*sorted([sorted(s1),sorted(s2)])))