class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # brute force O(n^2)
        n = len(energy)

        memo = { i : energy[i] for i in range(n) }

        # O(n)
        for i in range(n):
            start = i % k

            memo[start] += energy[i]

        print(memo)

        return max([ x[1] for x in memo.items() ])