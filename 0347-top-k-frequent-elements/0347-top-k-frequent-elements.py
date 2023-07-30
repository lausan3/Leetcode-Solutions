class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add all elements to a dictionary
        intDict = {}

        for num in nums:
            intDict[num] = intDict.get(num, 0) + 1

        # find max value while rK (number of most frequent numbers added) == k
        rK = 0
        newNums = []

        while rK < k:
            maxKey = max(intDict, key=intDict.get)

            newNums.append(maxKey)
            intDict[maxKey] = -1

            rK += 1

        return newNums