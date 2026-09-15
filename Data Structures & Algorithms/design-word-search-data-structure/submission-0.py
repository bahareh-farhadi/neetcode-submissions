class Node:
    def __init__(self):
        self.hashmap=dict()
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=Node()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char in curr.hashmap:
                curr=curr.hashmap[char]
            else:
                new_node=Node()
                curr.hashmap[char]=new_node
                curr=new_node
        curr.end=True
    
    def search_helper(self, word, root):
        if len(word)==0:
            if root.end==True:
                return True
            else:
                return False
        if word[0]!=".":
            if word[0] not in root.hashmap:
                return False
            else:
                return self.search_helper(word[1:], root.hashmap[word[0]])
        else:
            for char, node in root.hashmap.items():
                if self.search_helper(word[1:], node)==True:
                    return True
            return False
        

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)
        




        
