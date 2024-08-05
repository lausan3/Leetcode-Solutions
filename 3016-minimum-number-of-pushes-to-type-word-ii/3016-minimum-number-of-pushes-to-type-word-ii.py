class Solution:
    def minimumPushes(self, word: str) -> int:
        # add letters to a map
        freqMap = {}

        for ltr in word:
            if ltr not in freqMap:
                freqMap[ltr] = 0
            
            freqMap[ltr] += 1

        # sort freq map to get the most frequent letters
        freqMap = sorted(freqMap.items(), key=lambda item: item[1], reverse=True)
        print(freqMap)
        pressCount = 0

        for i in range(len(freqMap)):
            key, count = freqMap[i]
            
            if i < 8:
                pressCount += count
            elif i >= 8 and i < 16:
                pressCount += count * 2
            elif i >= 16 and i < 24:
                pressCount += count * 3
            else: 
                pressCount += count * 4


        return pressCount