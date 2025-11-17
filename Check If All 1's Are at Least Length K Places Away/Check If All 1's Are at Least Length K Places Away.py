class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr_spaces_away = -1

        for num in nums:
            if num == 1:
                if curr_spaces_away > -1 and curr_spaces_away < k:
                    return False

                curr_spaces_away = 0
            else:
                curr_spaces_away += 1

        return True