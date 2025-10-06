class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Simple frequency array O(2n) time O(1) space solution
        # freq = [0] * 3
        
        # for color in nums:
        #     freq[color] += 1

        # # populate colors in place
        # # O(n) since freq's values add up to the amount of colors in nums
        # i = 0
        # for color, color_freq in enumerate(freq):
        #     for _ in range(color_freq):
        #         nums[i] = color
        #         i += 1

        # 2. More complex three pointer O(n) time true O(1) space solution
        # pointers for where to swap numbers
        n = len(nums)
        if n < 2: return

        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            # if w < r and nums[w] == 0 and w + 1 < n:
            #     w += 1

            curr = nums[w]

            if curr == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
            # elif curr == 1:
            #     w += 1
            elif curr == 2:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1
            
            w += 1