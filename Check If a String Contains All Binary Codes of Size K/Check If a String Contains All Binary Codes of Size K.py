class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Brute force approach:
        1. Compute a set of all combinations of length k
        2. Perform a sliding window of length k, removing substrings
           from the set if not seen
        3. Return length == 0

        Time: O(n choose k)
        Space: O(n choose k)
        """
        combos = set(product('01', repeat=k))
        # join all tuples
        combos = set(map(lambda x: ''.join(x), combos))

        for i in range(len(s) - k):
            substr = s[i:i + k]

            if substr in combos:
                combos.remove(substr)

        return len(combos) == 0
