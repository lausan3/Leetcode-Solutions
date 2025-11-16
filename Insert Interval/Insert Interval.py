class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        """
        Brute Force Solution:
        
        maintain one hash map representing points along a given vertical line intersecting with the x-axis
        
        for each pair of columns (x1, y1), (x1, y2) and (x2, y1), (x2, y2), check for the smallest rectangle of these points
        """
        x_intersects = {}  # line centered at x : points on that line

        for x, y in points:
            if x not in x_intersects:
                x_intersects[x] = []

            x_intersects[x].append(y)

        seen = {}
        ans = float('inf')

        for x, intersect in sorted(x_intersects.items()):
            intersect.sort()

            # for each pair of points, calculate the area
            # in reverse so (y2 - y1) is positive when intersect is sorted
            for j, y2 in enumerate(intersect):
                for i in range(j):
                    y1 = intersect[i]

                    if (y1, y2) in seen:
                        area = (x - seen[y1,y2]) * (y2 - y1)
                        ans = min(ans, area)

                    seen[y1, y2] = x
        
        return ans if ans < float('inf') else 0