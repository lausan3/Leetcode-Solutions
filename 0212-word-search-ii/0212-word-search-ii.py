class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        head = self.root

        for ltr in word:
            if ltr not in head.children:
                head.children[ltr] = TrieNode()
            head = head.children[ltr]
        
        head.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        res, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])

        for word in words:
            trie.addWord(word)

        def dfs(r, c, node, word):
            # if out of bounds or visited or not a letter in one of the words
            if (r < 0 or c < 0 or
            r == ROWS or c == COLS or
            (r, c) in visit or board[r][c] not in node.children):
                return

            # mark as visited
            visit.add((r, c))

            ## valid character
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)