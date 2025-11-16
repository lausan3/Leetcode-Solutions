class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Math solution:
        
        Note: I noticed the similarity between the number of possible sides per number of points, but wasn't sure
         how to represent this. After looking through solutions, I learned it is through combinatorics.

        Since a side is chosen with two points, the number of sides that can be chose given n points along a y-intercept
         is n choose 2 or n * (n - 1) // 2.

        Time: O(n)
        Space: O(n)
        """
        MOD = 10**9 + 7

        y_to_points = {}

        for _, y in points:
            y_to_points[y] = y_to_points.get(y, 0) + 1

        res = 0
        total = 0
        # count number of lines/point pairs for each y
        for _, count in y_to_points.items():
            lines = count * (count - 1) // 2
            
            res = (res + total * lines) % MOD
            total = (total + lines) % MOD
        
        return res