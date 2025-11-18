class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        odd = len(bits) % 2 == 1

        if odd:
            return True
        else:
            return bits[-2] == 0