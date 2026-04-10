class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        original = image[sr][sc]

        def dfs(i, j):

            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or (i, j) in visited:
                return
            visited.add((i, j))
            if image[i][j] == original:
                image[i][j] = color
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)


        dfs(sr, sc)
        return image