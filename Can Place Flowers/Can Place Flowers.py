class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_to_place = n

        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and
                (i - 1 < 0 or (i - 1 >= 0 and flowerbed[i-1] == 0)) and
                (i + 1 >= len(flowerbed) or (i + 1 < len(flowerbed) and flowerbed[i+1] == 0))):
                flowerbed[i] = 1
                flowers_to_place -= 1

            if flowers_to_place == 0:
                return True

        return flowers_to_place == 0