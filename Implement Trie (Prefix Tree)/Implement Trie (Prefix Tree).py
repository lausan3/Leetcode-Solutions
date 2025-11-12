class TrieNode:
    def __init__(self, terminate: bool = False):
        self.terminate = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root

        for char in word:
            i = ord(char) - ord('a')

            if not temp.children[i]:
                temp.children[i] = TrieNode()

            temp = temp.children[i]

        temp.terminate = True

        print(f"{self.root.children}")

    def search(self, word: str) -> bool:
        temp = self.root

        for char in word:
            i = ord(char) - ord('a')

            if not temp.children[i]:
                return False

            temp = temp.children[i]

        return temp.terminate

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for i, char in enumerate(prefix):
            i = ord(char) - ord('a')

            if not temp.children[i]:
                return False

            temp = temp.children[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)