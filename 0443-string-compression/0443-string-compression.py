class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0  # count writing pointer
        i = 0  # list reading pointer

        while i < len(chars):
            letter = chars[i]
            count = 0

            # count amount of duplicate concurrent letters
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1

            # write amount to the character after the writing pointer
            chars[ans] = letter
            ans += 1
            if count > 1:
                # in case the count is >= 10
                for c in str(count):
                    chars[ans] = c
                    ans += 1

        return ans