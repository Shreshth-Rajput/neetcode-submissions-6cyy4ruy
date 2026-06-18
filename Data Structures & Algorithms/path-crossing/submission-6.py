class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        start = [0, 0]
        for p in path:
            visited.add(tuple(start))
            if p == "N":
                start[0] += 1
            elif p == "S":
                start[0] -= 1
            elif p == "E":
                start[1] += 1
            elif p == "W":
                start[1] -= 1
            if tuple(start) in visited:
                return True
        return False