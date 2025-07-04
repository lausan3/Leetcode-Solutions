class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # editorial solution:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))

        # old solution (not fast enough)
        # word = "a"

        # def get_next_letter(letter: str) -> str:
        #     a = ord('a')
        #     next_letter = (ord(letter) +  1 - a) % 26

        #     return chr(next_letter + a)

        # for op in operations:
        #     if len(word) > k:
        #         break

        #     if op == 0:
        #         word += word
        #     else:
        #         shifted_word = ""

        #         for letter in word:
        #             next_letter = get_next_letter(letter)
        #             shifted_word += next_letter

        #             if len(word) + len(shifted_word) > k:
        #                 break

        #         word += shifted_word

        # return word[k - 1]