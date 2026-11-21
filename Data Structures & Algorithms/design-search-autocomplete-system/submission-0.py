from typing import List

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.counts = dict() 

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.sentences = sentences
        self.times = times
        for i in range(len(self.sentences)):
            self.add_sentence(sentences[i], self.times[i])
        self.curr_sentence = ""
        self.curr_node = self.root
    
    def add_sentence(self, sentence, count):
        curr = self.root
        for char in sentence:
            if char not in curr.children:
                next_node = TrieNode()
                curr.children[char] = next_node
            curr = curr.children[char]
            if sentence not in curr.counts:
                curr.counts[sentence] = count
            else:
                curr.counts[sentence]+=count
           

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add_sentence(self.curr_sentence, 1)
            self.curr_sentence = ""
            self.curr_node = self.root
            return []
        if self.curr_node is None:
            self.curr_sentence+=c
            return []
        curr = self.curr_node
        if c not in curr.children:
            self.curr_sentence+=c
            self.curr_node = None
            return []
        else:
            curr = curr.children[c]
            self.curr_node = curr
            self.curr_sentence+=c
            # sort counts and return top 3
            sorted_dict = dict(sorted(curr.counts.items(), key=lambda item: (-item[1], item[0])))
            count = 0
            res = list()
            for key, val in sorted_dict.items():
                if count == 3:
                    return res
                res.append(key)
                count+=1
            return res
