class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        #cur = ord(keyboard[0])
        #movement = 0
        #for ch in word:
        #    movement  = movement + abs(ord(ch) - cur)
        #    cur = ord(ch)
        #return movement

        idx = {}
        dist = 0
        cur = 0
        for i, letter in enumerate(keyboard):
            idx[letter] = i
        
        for ch in word:
            dist = dist + abs(idx[ch] - cur)
            cur = idx[ch]

        return dist