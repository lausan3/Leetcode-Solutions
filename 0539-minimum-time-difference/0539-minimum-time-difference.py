class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(time: str):
            return (int(time[0:2]) * 60) + int(time[3:5])

        for i in range(len(timePoints)):
            timePoints[i] = convertToMinutes(timePoints[i])

        timePoints.sort()

        # normalize answer as maximum minutes in a day - max difference
        res = 1440 + timePoints[0] - timePoints[-1]

        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i - 1])

        return res