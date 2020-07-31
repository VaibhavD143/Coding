class Solution:
    def numWaterBottles(self, numBo: int, numEx: int) -> int:
        res = numBo
        full= numBo
        empty = 0
        
        while full>=numEx:
            full,empty = divmod(full,numEx)
            res+=full
            full = full+empty
        return res