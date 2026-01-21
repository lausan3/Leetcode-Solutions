class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Optimal Prefix Sum Solution:
        Because we can only move in two directions, left and right, we can use a prefix sum approach where
        we have two arrays where each cell includes the number of moves we have to do to move balls in the given direction.

        Time: O(n)
        Space: O(n)
        """
        n = len(boxes)
        ans = [0] * n

        balls_seen_left = 0
        balls_seen_right = 0
        total_left = 0
        total_right = 0

        for i in range(n):
            ans[i] += total_left
            balls_seen_left += int(boxes[i])
            total_left += balls_seen_left

            j = n - i - 1
            ans[j] += total_right
            balls_seen_right += int(boxes[j])
            total_right += balls_seen_right

        return ans
        """
        Brute Force O(n^2) solution:
        
        1. Note indices of each box with a ball in it
        2. For each box, i, append to an answer array the total distance of every other box with a ball to this box.
        
        Time: O(n^2)
        Space: O(n)
        
        Note: There may be a way to optimize this with two passes from left and right.
        """
        # ans = []
        # boxes_with_ball = []
        
        # for i, c in enumerate(boxes):
        #     if c == '1':
        #         boxes_with_ball.append(i)
                
        # for i in range(len(boxes)):
        #     total_dist = 0
            
        #     for box_index in boxes_with_ball:
        #         total_dist += abs(i - box_index)
            
        #     ans.append(total_dist)
            
        # return ans