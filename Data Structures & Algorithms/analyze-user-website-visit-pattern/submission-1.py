class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        combined = list(zip(timestamp, username, website))
        combined.sort()
        mp = defaultdict(list)
        for ts, un, ws in combined:
            mp[un].append(ws)
        count = defaultdict(int)
        for un in mp:
            patterns = set()
            patterns.update(combinations(mp[un], 3))
            print(patterns)
            for pattern in patterns:
                count[pattern] += 1
        max_count = 0
        res = tuple()
        for pattern in count:
            if count[pattern] > max_count or (count[pattern] == max_count and pattern < res):
                max_count = count[pattern]
                res = pattern
        return list(res)