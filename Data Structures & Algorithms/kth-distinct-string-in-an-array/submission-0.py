class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_count = dict()
        distinct = list()
        for s in arr:
            distinct_count[s] = distinct_count.get(s, 0) + 1
            if distinct_count[s] == 1:
                distinct.append(s)
            else:
                if s in distinct:
                    distinct.remove(s)
        if k <= len(distinct):
            return distinct[k-1]
        return ""