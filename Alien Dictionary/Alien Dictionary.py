class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Intuition:

        If each letter is a node in a graph, then there are directed edges between certain letters and ones the come after.

        Since we are trying to check if it's possible to sort the language lexicographically, this is similar
         to checking if the graph (letters) have a cycle or not. If the claim is correct, there will not be cycles or 
         unreachable letters.

        Therefore, the intuitive approach would be to perform topological sort on the graph of letters in the word list.

        Time: O(C) where C = length of all words appended to each other. comes from first Zip func since we are testing words
         one after another.

        Space: O(U + min(U^2, N)) where U is the number of unique letters (constrained to 26 in the description), and N is 
         the number of words.
        """
        letters = collections.defaultdict(set)
        inbound = Counter({a: 0 for word in words for a in word })

        # O(C)
        for word1, word2 in zip(words, words[1:]):
            # the key here is that since the words are claimed to be lexicographically sorted, we only care about where
            #  the letters first differ and hence that's where our edges come from.
            for a, b in zip(word1, word2):
                if a != b:
                    if b not in letters[a]:
                        letters[a].add(b)

                        inbound[b] = inbound.get(b, 0) + 1

                    break
            else:  # check that second word isn't a prefix of the first word, since prefixes should always come first.
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
        
        return order if len(order) == len(inbound) else ""