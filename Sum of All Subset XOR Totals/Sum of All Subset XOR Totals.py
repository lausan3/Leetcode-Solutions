class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # O(2^n)
        # Modify a generic generateSubsets function to calculate a running XOR
        def XORSum(i: int, curr_xor: int) -> int:
            if i >= n:
                return curr_xor

            with_element = XORSum(i + 1, curr_xor ^ nums[i])

            without_element = XORSum(i + 1, curr_xor)

            return with_element + without_element


        return XORSum(0, 0)