class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Approach: 
        #  Sort the meetings by start days
        #  Merge the meetings
        #  Sum the difference of next start meeting time and 
        #   current meeting end time.

        # Time: O(n log n) from sorting.
        # Space: O(n) since we are making a copy of the meetings array.
        meetings.sort(key=lambda x: x[0])

        merged = []
        
        for start, end in meetings:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        available_days = merged[0][0] - 1
        for i in range(len(merged)):
            if i == len(merged) - 1:
                available_days += days - merged[-1][1]
                break

            _, end = merged[i]
            next_start, _ = merged[i+1]

            available_days += next_start - end - 1

        return available_days