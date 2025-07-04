class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word = "a"

        def get_next_letter(letter: str) -> str:
            a = ord('a')
            next_letter = (ord(letter) +  1 - a) % 26

            return chr(next_letter + a)

        for op in operations:
            if len(word) > k:
                break

            if op == 0:
                word += word
            else:
                shifted_word = ""

                for letter in word:
                    next_letter = get_next_letter(letter)
                    shifted_word += next_letter

                    print(f"{letter=}, {next_letter=}, {shifted_word=}")

                word += shifted_word

        return word[k - 1]