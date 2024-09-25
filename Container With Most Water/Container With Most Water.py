class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left <= right:
            left_height, right_height = height[left], height[right]
            area = min(left_height, right_height) * (right - left)

            max_area = max(max_area, area)

            if left_height > right_height:
                right -= 1
            else:
                left += 1

        return max_area