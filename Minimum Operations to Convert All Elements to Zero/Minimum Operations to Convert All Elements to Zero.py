class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Monotonic stack solution (editorial):

            maintain a monotonically increasing stack
            ignoring 0s, if the stack is empty or monotonicity is broken, add one to
            operations count

        Time: O(n)
        Space: O(n)

        Note: This is a totally unintuitive solution. I'll write the intuitive but slow 
        one below.
        """
        monotonic_stk = []
        res = 0

        for num in nums:
            while monotonic_stk and monotonic_stk[-1] > num:
                monotonic_stk.pop()
            if num == 0:
                continue
            elif not monotonic_stk or monotonic_stk[-1] < num:
                monotonic_stk.append(num)
                res += 1

        return res