class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si = iter(s)
        for i, t_char in enumerate(t):
            for si_char in si:
                if si_char == t_char:
                    break
            else:
                return len(t) - i 

        return 0
