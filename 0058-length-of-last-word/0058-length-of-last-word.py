class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stack = []
        newWord = False

        for char in s:
            # if the current character isn't whitespace and we 
            if char != " " and newWord == False:
                stack.append(char)
            # if the current character isn't whitespace but we have looked at a word
            # before, clear the stack
            elif char != " " and newWord == True:
                del stack[:]
                newWord = False
                stack.append(char)
            else:
                newWord = True

        return len(stack)