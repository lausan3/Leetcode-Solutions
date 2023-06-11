class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        limit = t - 3000

        # append new ping
        self.queue.append(t)

        # remove any pings that are not in the range (t - 3000, t).
        # iterating over self.queue[:] iterates over a copy of the array instead of of the normal in-order shift
        for num in self.queue[:]:
            if num < limit:
                self.queue.pop(0)
            else:
                break
        
        # return length of the queue
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)