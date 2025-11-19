class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
        Brute force solution is quite easy, but O(n log n).

        Maybe there's a math solution to it? something to do with finding all nums that
        are evenly divisible by original?

        Nah, just maintaining a set is enough and makes it O(n) O(n).
        """
        hashset = set(nums)

        while original in hashset:
            original *= 2
        
        return original