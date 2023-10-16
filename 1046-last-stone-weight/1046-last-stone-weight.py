class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we have to use the negative versions in python because we want a max heap, heapq is weird
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # keep playing the game until there is one or no stones
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            # weights are equal, pop from the back (largest 2)
            if y > x:
                heapq.heappush(stones, x - y)
            
        stones.append(0) # just in case no more stones
        return abs(stones[0])