class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_address = set()
        col_address = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (matrix[row][col] == 0):
                    row_address.add(row)
                    col_address.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in row_address or col in col_address:
                    matrix[row][col] = 0
        
        