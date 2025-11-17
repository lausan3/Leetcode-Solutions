class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Intuition:

        If each letter is a node in a graph, then there are directed edges between certain letters and ones the come after.

        Since we are trying to check if it's possible to sort the language lexicographically, this is similar
         to checking if the graph (letters) have a cycle or not. If the claim is correct, there will not be cycles or 
         unreachable letters.

        Therefore, the intuitive approach would be to perform topological sort on the graph of letters in the word list.
        """
        letters = collections.defaultdict(set)
        inbound = Counter({a: 0 for word in words for a in word })

        for word1, word2 in zip(words, words[1:]):
            for a, b in zip(word1, word2):
                if a != b:
                    if b not in letters[a]:
                        letters[a].add(b)

                        inbound[b] = inbound.get(b, 0) + 1

                    break
            else:  # check that second word isn't a prefix of the first word
                if len(word2) < len(word1):
                    return ""

        q = collections.deque()
        q.extend([ a for a in inbound if inbound[a] == 0])

        order = ""

        # topological sort
        while q:
            letter = q.popleft()

            order += letter

            for after in letters[letter]:
                inbound[after] -= 1

                if inbound[after] == 0:
                    q.append(after)

        if len(order) < len(inbound):
            return ""
        
        return order