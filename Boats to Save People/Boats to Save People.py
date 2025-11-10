class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = SortedList()

        for weight in people:
            i = boats.bisect_right(weight)

            if i >= len(boats):
                boats.add(weight)
            else:
                old_weight = boats.pop(i - 1)
                boats.add(old_weight - weight)

            print(f"Added {weight}. {boats=}")

        return len(boats)
