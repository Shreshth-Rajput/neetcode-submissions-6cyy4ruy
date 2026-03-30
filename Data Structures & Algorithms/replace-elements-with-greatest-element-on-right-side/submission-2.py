class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest_value = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = highest_value
            if temp > highest_value:
                highest_value = temp
        return arr