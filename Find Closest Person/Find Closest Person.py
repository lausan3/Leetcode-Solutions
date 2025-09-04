class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first = 0

        x_dist = abs(z - x)
        y_dist = abs(z - y)

        if x_dist < y_dist:
            first = 1

        if y_dist < x_dist:
            first = 2

        return first