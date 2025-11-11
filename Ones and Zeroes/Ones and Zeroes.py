class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        idx_to_freq = {} # index -> (zero count, ones count)

        # count 0s and 1s
        count = 0
        
        for i, s in enumerate(strs):
            if len(s) > m + n:
                continue

            z = o = 0

            for char in s:
                match char:
                    case '0':
                        z += 1
                    case '1':
                        o += 1

            idx_to_freq[i] = (z, o)

        freqs_sorted = sorted(idx_to_freq.values())
        z = o = 0

        for zer, one in freqs_sorted:
            if z + zer <= m and o + one <= n:
                z += zer
                o += one
                count += 1

        return count
