class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) Time, O(1) Space
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        water_count = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                water_count += max_l - height[l]
                # because we did max then add to count, new maxes won't count toward water count
            else:
                r -= 1
                max_r = max(max_r, height[r])
                water_count += max_r - height[r]
                
        return water_count