class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not len(s) % 2:
            even = True
        else:
            even = False
            only_one = True
        count = Counter(s)
        for occur in count.values():
            if occur % 2 == 1:
                if even:
                    return False
                else:
                    if only_one:
                        only_one = False
                    else:
                        return False
        return True