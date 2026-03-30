class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_mag = Counter(magazine)
        for ch in count_ransom:
            if not (count_mag[ch] / count_ransom[ch]) >= 1:
                return False
        return True