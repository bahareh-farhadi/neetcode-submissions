class Node:
    def __init__(self):
        self.hashmap=dict()
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=Node()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char in curr.hashmap:
                curr=curr.hashmap[char]
            else:
                new_node=Node()
                curr.hashmap[char]=new_node
                curr=new_node
        curr.end=True



    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            if char in curr.hashmap:
                curr=curr.hashmap[char]
            else:
                return False
        if curr.end==True:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for char in prefix:
            if char in curr.hashmap:
                curr=curr.hashmap[char]
            else:
                return False
        return True
        
        