class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
            
        triangle = [
            [1], [1, 1]
        ]

        for i in range(2, numRows):
            last_row = triangle[i - 1]
            row = [1]

            for j in range(1, i):
                row.append(last_row[j - 1] + last_row[j])

            row.append(1)

            triangle.append(row)
        
        return triangle