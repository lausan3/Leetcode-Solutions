class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Note: Thinking about a DP solution similar to maximum plus size?
        
        Simple DFS Solution (TLE):
        
        For each cell, return longest increasing path in the matrix
        from this cell
        
        
        Space: O(n * m)
        """
        m = len(matrix)
        n = len(matrix[0])
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        visited = set()
        
        def dfs(r, c, path_len) -> int:
            if (0 > r >= m or
                0 > c >= n):
                return path_len
            
            visited.add((r, c))
            max_path_len = path_len
            
            for dx, dy in dirs:
                new_r, new_c = r + dx, c + dy
                if (0 <= new_r < m and
                    0 <= new_c < n and
                    matrix[new_r][new_c] > matrix[r][c]
                   ):
                    max_path_len = max(max_path_len, dfs(new_r, new_c, path_len + 1))
                    
            visited.remove((r, c))
            return max_path_len
        
        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c, 1))
                
        return res