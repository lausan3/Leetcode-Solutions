class TrieNode:
    def __init__(self, terminate: bool = False):
        self.terminate = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root

        for char in word:
            i = ord(char) - ord('a')

            if not temp.children[i]:
                temp.children[i] = TrieNode()

            temp = temp.children[i]

        temp.terminate = True

    def search(self, word: str) -> bool:
        temp = self.root

        return self.dfs(0, temp, word)

    def dfs(self, i: int, node: TrieNode, word: str) -> bool:
        n = len(word)

        if i == n:
            return node.terminate

        temp = node

        char = word[i]

        if char == ".":
            available = list(filter(lambda x: x, temp.children))

            for available_char in available:
                if self.dfs(i + 1, available_char, word):
                    return True

            return False
        else:
            j = ord(char) - ord('a')

            if not temp.children[j]:
                return False

            temp = temp.children[j]

        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)