class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        keyed = defaultdict(list)
        for s in strings:
            key = tuple((ord(s[i]) - ord(s[i-1])) % 26 for i in range(1, len(s)))
            keyed[key].append(s)
        return list(keyed.values())