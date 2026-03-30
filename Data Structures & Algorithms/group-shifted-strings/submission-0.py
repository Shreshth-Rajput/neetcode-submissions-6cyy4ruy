class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifted = defaultdict(list)
        for s in strings:
            key = tuple((ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s)))
            shifted[key].append(s)
        return list(shifted.values())
        # ascii of all alphabets.
        # difference would be the same.