class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                leftVal = self.prefix[row - 1][col] if row > 0 else 0
                topVal = self.prefix[row][col - 1] if col > 0 else 0
                topLeftVal = self.prefix[row - 1][col - 1] if row > 0 and col > 0 else 0
                self.prefix[row][col] = leftVal + topVal - topLeftVal + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        leftVal = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        topVal = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        topLeftVal = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.prefix[row2][col2] - leftVal - topVal + topLeftVal


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
