class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = set()
        s2_words = set()
        result = set()

        # O(s1)
        for word in s1.split():
            if word not in s1_words:
                s1_words.add(word)
            else:
                s1_words.remove(word)


        # O(s2)
        for word in s2.split():
            if word not in s2_words:
                s2_words.add(word)
            else:
                s2_words.remove(word)

        for word in s1_words:
            if word not in result and word not in s2_words:
                result.add(word)

        for word in s2_words:
            if word not in result and word not in s1_words:
                result.add(word)        

        return list(result)