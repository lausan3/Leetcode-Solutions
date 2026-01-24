class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.current_query = ""
        self.sentence_frequency = {}
        
        for sentence, frequency in zip(sentences, times):
            self.sentence_frequency[sentence] = (
                self.sentence_frequency.get(sentence, 0) + frequency
            )
            
        self.order_sentences()
        
        
    def order_sentences(self):
        sentences = self.sentence_frequency.items()
        
        sorted_sentences = sorted(list(sentences), key=lambda grp: (-grp[1], grp[0]))
        
        self.sentence_frequency = { k : v for k, v in sorted_sentences }

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.sentence_frequency[self.current_query] = (
                self.sentence_frequency.get(self.current_query, 0) + 1
            )
                
            self.order_sentences()
            
            self.current_query = ""
            
            return []
        
        self.current_query += c
        
        res = []
        
        for sentence, _ in self.sentence_frequency.items():
            if len(res) == 3:
                break
            elif sentence.startswith(self.current_query):
                res.append(sentence)
        
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)