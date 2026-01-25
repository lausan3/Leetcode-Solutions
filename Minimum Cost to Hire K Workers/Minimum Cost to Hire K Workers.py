class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        Editorial Max Heap Sliding Window Approach:
        We notice that we want to prioritize the lowest ratio workers since 
         they give us a lower overall cost
        This tells us that we should maintain a sliding window using a max heap,
         popping off the largest ratios when it grows too big.

        Time: O(n log n + n log k). From sorting n and maintaining heap of length k.
        Space: O(n + k)
        """
        n = len(quality)
        min_cost = float("inf")
        current_total_quality = 0
        wage_to_quality_ratio = []

        # calculate wage_to_quality_ratios for each worker
        for i in range(n):
            ratio = wage[i] / quality[i]
            wage_to_quality_ratio.append( (ratio, quality[i]) )
        
        # sort by lowest ratios
        wage_to_quality_ratio.sort(key=lambda x: x[0])

        # our max heap
        workers = []

        for i in range(n):
            ratio, quality = wage_to_quality_ratio[i]

            heapq.heappush(workers, -quality)
            current_total_quality += quality

            if len(workers) > k:
                current_total_quality += heapq.heappop(workers)
            
            if len(workers) == k:
                min_cost = min(
                    min_cost,
                    current_total_quality * ratio   
                )

        return min_cost