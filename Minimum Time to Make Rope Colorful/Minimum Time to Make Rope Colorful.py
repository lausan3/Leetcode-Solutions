class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Two pointer approach:
        # for each pair of adjacent balloons, 
        #   if they're the same color, 
        #       add the one with a less time to remove to sum
        #       propagate the highest cost balloon up (as a way to remove largest time ones)
        # return sum
        # 
        # Time: O(n), Space: O(1)

        n = len(colors)
        
        minTimeNeeded = 0

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                minTimeNeeded += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return minTimeNeeded