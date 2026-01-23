class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Brute Force:
        
        1. Init n = number of dominos
        2. Count indices of each value from 1 -> 6 in top and bottom dominos
        3. For each value 1 -> 6, if each index is different from each other,
           calculate the swap by doing n - max(len(top), len(bottom))
        """
        n = len(tops)
        top_values = { i : set() for i in range(1, 7)}
        bottom_values = { i : set() for i in range(1, 7) }
        
        for i in range(n):
            top_values[tops[i]].add(i)
            bottom_values[bottoms[i]].add(i)
    
        res = float('inf')
            
        for value in range(1, 7):
            top = top_values[value]
            bottom = bottom_values[value]
            
            combined = top.union(bottom)
            
            if len(combined) == n:
                min_swaps = n - max(len(top), len(bottom))
                res = min(res, min_swaps)
                
        return -1 if res == float('inf') else res