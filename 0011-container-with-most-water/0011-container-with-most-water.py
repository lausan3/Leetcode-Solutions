class Solution:
    def maxArea(self, height: List[int]) -> int:
        # this is a two pointer problem
        # where we adjust pointers based on which pointer value is lower because the higher value has a higher chance of
        # being part of a larger area
        begin = 0
        end = len(height) - 1
        maxArea = 0

        # edge case
        ## if there's only two values
        if (len(height) == 2):
            return height[begin] if height[begin] < height[end] else height[end]

        for i in range(len(height)):
            # get area
            width = end - begin
            area = height[begin] * width if height[begin] < height[end] else height[end] * width

            # compare area with maxArea
            maxArea = area if area > maxArea else maxArea

            # adjust pointer
            ## begin less than height, adjust less by 1
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1

        return maxArea