class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        bit_mapping = [0] * (len(grid)**2)
        output = [0] * 2
        for i in grid:
            for j in i:
                bit_mapping[j - 1] += 1

        for e, bit in enumerate(bit_mapping):
            if bit == 0:
                output[1] = e + 1
            elif bit == 2:
                output[0] = e + 1

        return output