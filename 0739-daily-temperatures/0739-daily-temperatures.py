class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        monotonicStk = answer = []  # make a stack of pairs temperature : day index
        answer = [0 for i in range(n)]

        # backwards traverse
        for i in range(n - 1, -1, -1):
            currTemp = temperatures[i]

            # pop temperatures off the stack until we see one that is greater than or equal to currTemp
            while monotonicStk and currTemp >= monotonicStk[-1][0]:
                monotonicStk.pop()
            
            # mark the distance accordingly if it's greater than currTemp
            if monotonicStk and monotonicStk[-1][0] > currTemp:
                answer[i] = monotonicStk[-1][1] - i

            monotonicStk.append([currTemp, i])

        return answer