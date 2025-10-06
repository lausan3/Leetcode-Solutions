class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Simple frequency array O(2n) time O(1) space solution
        freq = [0] * 3
        
        for color in nums:
            freq[color] += 1

        # populate colors in place
        # O(n) since freq's values add up to the amount of colors in nums
        i = 0
        for color, color_freq in enumerate(freq):
            for _ in range(color_freq):
                nums[i] = color
                i += 1

        # More complex three pointer O(n) time true O(1) space solution