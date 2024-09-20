class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Time: O(n). Space: O(n)

        party_counts = Counter(senate)
        i = 0

        while party_counts["R"] > 0 and party_counts["D"] > 0:
            if i >= len(senate):
                i = 0

            move = "D" if senate[i] == "R" else "R"

            party_counts[move] -= 1

            i += 1

        return "Radiant" if party_counts["R"] > 0 else "Dire"