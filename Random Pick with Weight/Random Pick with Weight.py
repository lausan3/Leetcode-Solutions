class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.total = sum(w)


        self.probs = []

        acc = 0
        for weight in w:
            acc += weight
            self.probs.append(acc)

    def pickIndex(self) -> int:
        prob = random.random() * self.total

        i = bisect.bisect(self.probs, prob)

        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()