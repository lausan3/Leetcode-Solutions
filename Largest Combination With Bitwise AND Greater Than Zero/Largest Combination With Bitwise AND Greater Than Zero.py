class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_size = 0

        # for 24 bits in possible 10^5 num (from constraints)
        for i in range(24):
            size = 0

            # for every position in 24 bit string, find the 
            # max amount of candidates that have a 1 at 
            # that position, solution is the max of 
            # these calculations.
            for num in candidates:
                if num & (1 << i) != 0:
                    size+=1

            max_size = max(max_size, size)

        return max_size