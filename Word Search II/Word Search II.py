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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        t = Trie()
        result = set()
        starts = set([ word[0] for word in words ])

        for word in words:
            t.insert(word)

        # up, down, left, right
        dirs = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        visited = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or r == m or
                c < 0 or c == n or
                (r, c) in visited
            ):
                return

            i = ord(board[r][c]) - ord('a')

            if not node.children[i]:
                return

            visited.add((r, c))
            node = node.children[i]
            word += board[r][c]

            if node.terminate:
                result.add(word)

            for row, col in dirs:
                dr, dc = r + row, c + col

                dfs(dr, dc, node, word)

            visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                if board[r][c] in starts:
                    dfs(r, c, t.root, "")

        return list(result)
