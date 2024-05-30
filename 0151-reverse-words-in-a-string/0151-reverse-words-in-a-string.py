class Solution:
    def reverseWords(self, s: str) -> str:
        splitArr = s.split()
        res = ""

        print(splitArr)

        for i, word in enumerate(splitArr[::-1]):
            if word != " ":
                res += f"{word} " if i < len(splitArr) - 1 else word 
                
        return res