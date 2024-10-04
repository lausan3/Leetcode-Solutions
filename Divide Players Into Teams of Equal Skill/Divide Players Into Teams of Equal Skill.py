class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        # sort array
        # keep note of the skill combination we need to match
        # loop through half of the array
        #   pair the player at i and player at n - i
        #   if their combined total != required skill total, return -1
        #   else add their chemistry
        
        # Time: O(n log n), Space: O(1)

        n = len(skill)
        skill.sort()

        req_total = skill[0] + skill[-1]
        chemistry_total = 0

        for i in range(n // 2):
            p1, p2 = skill[i], skill[n - i - 1]

            if p1 + p2 != req_total:
                return -1

            chemistry_total += p1 * p2

        return chemistry_total