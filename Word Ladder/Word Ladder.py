class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Initial thoughts:
        I think something like Djikstras would work well here.
        If each word is a node and has undirected edges to every other
        word that only has one letter different, then we can traverse
        the graph until we get from beginWord to endWord and take the
        shortest path.
        
        BFS Approach:

        1. Construct graph
        2. Perform BFS
        """
        if endWord not in wordList:
            return 0

        graph = { word : set() for word in wordList }
        graph[beginWord] = set()

        for out in wordList:
            for into in wordList:
                if out == into:
                    continue
                
                diff_count = sum(1 for a, b in zip(out, into) if a != b)

                if diff_count == 1:
                    graph[out].add(into)
                    graph[into].add(out)

        for into in wordList:
            diff_count = sum(1 for a, b in zip(beginWord, into) if a != b)

            if diff_count == 1:
                graph[beginWord].add(into)
                graph[into].add(beginWord)

        start = (beginWord, 1)
        q = collections.deque([start])
        visited = set()
        min_transforms = float('inf')

        while q:
            word, path_len = q.popleft()
            print(f"from {word}. length {path_len}")

            visited.add(word)

            if word == endWord:
                min_transforms = min(min_transforms, path_len)
                print(f"new length: {min_transforms}")

            for next_word in graph[word]:
                if next_word in visited:
                    continue
                
                q.append( (next_word, path_len + 1) )
                print(f"to {next_word}")

        return min_transforms if min_transforms != float('inf') else 0