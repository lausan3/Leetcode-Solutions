class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_sum = digits[-1] + 1
        digits[-1] = digit_sum % 10
        carry = digit_sum == 10

        if not carry: return digits

        i = len(digits) - 2 # we've already added one to the end

        while carry and i >= 0:
            digit_sum = digits[i] + 1
            digits[i] = digit_sum % 10
            carry = digit_sum == 10
            i -= 1
        
        # account for leading zero, means we need to add one to the beginning
        if carry and digits[0] == 0:
            digits.insert(0, 1)

        return digits