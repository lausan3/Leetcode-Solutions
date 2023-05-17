class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        smallestWordIndex = 0

        for index, word in enumerate(strs):
            if len(word) < len(strs[smallestWordIndex]):
                smallestWordIndex = index

        for index, char in enumerate(strs[smallestWordIndex]):
            sameLetter = True
            for word in strs:
                if char != word[index]:
                    return commonPrefix
            
            commonPrefix += strs[smallestWordIndex][index]

        return commonPrefix