class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n = len(picture)
        m = len(picture[0])
        column_count = [0] * m
        row_count = [0] * n
        res = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B":
                    row_count[i] += 1
                    column_count[j] += 1 
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B" and column_count[j] == row_count[i] == 1:
                    res += 1
                    
        return res