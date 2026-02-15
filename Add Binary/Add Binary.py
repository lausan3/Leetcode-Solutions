class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Note: was initially going for the bit-by-bit solution, but there's too many edge
         cases for me to stay interested in implementing it.

        Editorial Bit Manip Approach:

        Time: O(m + n)
        Space: O(max(m, n))
        """
        res, carry = int(a, 2), int(b, 2)

        while carry:
            res, carry = res ^ carry, (res & carry) << 1

        return bin(res)[2:]
