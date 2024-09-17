class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for cost in nums:
            # the max is the decision of skipping rob2 and robbing the current house + rob1 or
            # just robbing rob2.
            rob1, rob2 = rob2, max(rob1 + cost, rob2)

        return rob2