class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            # if the current character is the first letter in the needle, start piecing together a word
            if haystack[i] == needle[0]:
                for index, char in enumerate(haystack[i:]):
                    # if the character isn't the same as the same postion in the needle, then break
                    # and try again from the next i value
                    if char != needle[index]:
                        break
                    
                    if index >= len(needle) - 1:
                        return i

        return -1