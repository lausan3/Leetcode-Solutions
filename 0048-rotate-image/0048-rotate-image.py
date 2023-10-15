class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        if(matrix == None or len(matrix) == 0 or len(matrix[0]) == 0): return
        rows = len(matrix)
        cols = len(matrix[0])
        
        first, last = 0, rows - 1
        
        # swap ith row with (n - i)th row
        while(first<last):
            matrix[first], matrix[last] = matrix[last], matrix[first]
            first += 1
            last -= 1
        
        # transpose edges (rows -> columns, columns -> rows)
        for i in range(0,rows):
            for j in range(i + 1,cols):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]