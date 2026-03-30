class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > (len(flowerbed) / 2) + 1:
            return False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    n -= 1
                    flowerbed[i] = 1
            if n <= 0:
                return True
        return False