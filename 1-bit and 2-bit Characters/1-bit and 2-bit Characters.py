class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
            
        return bits[-2] == 0