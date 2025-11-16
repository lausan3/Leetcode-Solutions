class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        total = sum(w)


        self.probs = []

        acc = 0
        for weight in w:
            acc += weight / total
            self.probs.append(acc)

    def pickIndex(self) -> int:
        prob = random.uniform(0.0, 100.0)

        i = bisect.bisect_left(self.probs, prob)

        return i - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()