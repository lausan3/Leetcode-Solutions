class Solution:
    def decodeString(self, s: str) -> str:
        """
        Editorial Brute Force Stack Approach:
        Maintain a number stack and string stack, using them to
         construct the result string.

        Time: O(maxK * n) where n is the length of s
        Space: O(m + n) where m is the number of letters we have
        """
        num_stack = []
        str_stack = []
        res = ""
        k = 0

        for c in s:
            # maintain k
            if c.isnumeric():
                k = k * 10 + int(c)
            # start capturing by appending k
            elif c == "[":
                num_stack.append(k)
                k = 0

                str_stack.append(res)
                res = ""
            # end capture by appending current string k times
            elif c == "]":
                decoded = str_stack.pop()
                decoded += res * num_stack.pop()

                res = decoded
            else:
                res += c

        return res