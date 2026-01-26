class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        nums = sorted(arr)
        pairs = defaultdict(list)

        for n1, n2 in zip(nums[:-1], nums[1:]):
            diff = n2 - n1

            pairs[diff].append([n1, n2])

        return min(pairs.items(), key=lambda grp: grp[0])[1]