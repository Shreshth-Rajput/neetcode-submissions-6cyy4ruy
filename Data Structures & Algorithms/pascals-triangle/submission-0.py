class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[0] * n for n in range(1, numRows + 1)]
        for i in range(0, numRows):
            for j in range(i + 1):
                if j == 0 or j == i or i == 0:
                    triangle[i][j] = 1
                else:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j] 
        return triangle