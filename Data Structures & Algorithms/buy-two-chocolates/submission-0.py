class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float("inf"), float("inf")
        lp = len(prices)
        if lp < 2:
            return money
        for price in prices:
            if min1 > price:
                tmp = min1
                min1 = price
                min2 = tmp
            elif min2 > price:
                min2 = price
        k = money - min1 - min2
        return k if k >= 0 else money