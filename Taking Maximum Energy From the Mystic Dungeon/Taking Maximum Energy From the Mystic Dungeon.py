class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # brute force O(n^2)
        max_energy = float("-inf")
        n = len(energy)

        # O(n^2)
        for start in range(n):
            current_energy = 0
            curr_wiz = start

            while curr_wiz < n:
                current_energy += energy[curr_wiz]

                curr_wiz += k

            max_energy = max(max_energy, current_energy)

        return max_energy