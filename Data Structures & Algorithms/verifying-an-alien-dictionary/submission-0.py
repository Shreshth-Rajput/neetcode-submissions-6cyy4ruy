class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        order_dict = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            w0, w1 = words[i - 1], words[i]
            for j in range(len(w0)):
                if j == len(w1):
                    return False
                if w0[j] != w1[j]:
                    if order_dict[w0[j]] > order_dict[w1[j]]:
                        return False
                    break
        return True
