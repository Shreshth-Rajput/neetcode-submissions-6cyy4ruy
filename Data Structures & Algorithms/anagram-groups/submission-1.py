class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]
        anagrams = list()
        for i, s1 in enumerate(sorted_strs):
            temp_list = list()
            temp_list.append(strs[i])
            for j, s2 in enumerate(sorted_strs):
                if s1 == s2 and i != j:
                    temp_list.append(strs[j])
            temp_list.sort()
            if temp_list not in anagrams:
                anagrams.append(temp_list) 
        return anagrams