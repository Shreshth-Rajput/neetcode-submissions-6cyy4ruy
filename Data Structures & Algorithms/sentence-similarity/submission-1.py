class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if not len(sentence1) == len(sentence2):
            return False
        pairs = defaultdict(set)
        for p1, p2 in similarPairs:
            pairs[p1].add(p2)
            pairs[p2].add(p1)
        for i in range(len(sentence1)):
            if not (sentence1[i] == sentence2[i] or sentence2[i] in pairs[sentence1[i]]):
                return False
        return True