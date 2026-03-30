class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_count = dict()
        for s in arr:
            distinct_count[s] = distinct_count.get(s, 0) + 1
        for s in arr:
            if distinct_count[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""