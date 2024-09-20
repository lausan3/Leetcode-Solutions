class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Time: O(n). Space: O(n)

        n = len(senate)
        rad = deque()
        dire = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i)

        while rad and dire:
            rad_senator = rad.popleft()
            dire_senator = dire.popleft()

            if rad_senator < dire_senator:
                n += 1
                rad.append(n)
            else:
                dire.append(n)

        return "Radiant" if rad else "Dire"