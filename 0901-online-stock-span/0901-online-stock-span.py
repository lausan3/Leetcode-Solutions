class StockSpanner:

    def __init__(self):
        self.stk = []  # decreasing monotonic stack of [price : amount of days before it that were <=]

    # approach: keep popping off items that are less than next price while incrementing a count, then append
    # to the stack [price : count]
    def next(self, price: int) -> int:
        stk = self.stk
        consecutiveLess = 1

        while stk and stk[-1][0] <= price:
            consecutiveLess += stk[-1][1]
            stk.pop()

        stk.append([price, consecutiveLess])

        return consecutiveLess


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)