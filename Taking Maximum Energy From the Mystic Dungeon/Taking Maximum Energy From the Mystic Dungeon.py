class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # brute force O(n) space O(1)
        n = len(energy)

        result = -inf

        # O(n)
        for i in range(n - k, n):
            running_energy = 0
            j = i

            while j >= 0:
                running_energy += energy[j]
                result = max(result, running_energy)
                j -= k
        
        return result