class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * (n + 1)
        outgoing = [0] * (n + 1)
        for i in range(len(trust)):
            incoming[trust[i][1]] += 1
            outgoing[trust[i][0]] += 1
        for i in range(1, n + 1):
            if outgoing[i] == 0:
                if incoming[i] == n - 1:
                    return i
        return -1