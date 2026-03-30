class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)

        return list(anagrams.values())