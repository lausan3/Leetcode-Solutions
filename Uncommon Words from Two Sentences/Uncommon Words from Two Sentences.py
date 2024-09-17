class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = {}
        s2_words = {}
        result = set()

        # O(s1)
        for word in s1.split():
            s1_words[word] = s1_words.get(word, 0) + 1

        # O(s2)
        for word in s2.split():
            s2_words[word] = s2_words.get(word, 0) + 1


        for word, count in s1_words.items():
            if count == 1 and word not in result and word not in s2_words:
                result.add(word)

        for word, count in s2_words.items():
            if count == 1 and word not in result and word not in s1_words:
                result.add(word)        

        return list(result)

        # Cool solution I found on LeetCode:
        # # Split the sentences into words
        # words_s1 = s1.split()
        # words_s2 = s2.split()
        
        # # Combine all words into one list
        # all_words = words_s1 + words_s2
        
        # # Count the frequency of each word
        # word_count = Counter(all_words)
        
        # # Find words that occur exactly once
        # return [word for word in word_count if word_count[word] == 1]