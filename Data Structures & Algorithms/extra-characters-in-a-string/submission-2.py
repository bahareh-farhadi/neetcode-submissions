class TrieNode:
    def __init__(self):
        self.children={} #map char to its TrieNode
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def add_word(self, word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                new_node=TrieNode()
                curr.children[char]=new_node
            curr=curr.children[char]
        curr.isEnd=True
    
    def search_word(self, word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr=curr.children[char]
        return curr.isEnd          
        
        
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie_root=Trie()
        for word in dictionary:
            trie_root.add_word(word)
        dp=list()
        for i in range(len(s)+1):
            dp.append(float('inf'))
        dp[-1]=0
        for i in range(len(dp)-2, -1, -1):
            dp[i]=1+dp[i+1]
            for j in range(i, len(s)):
                if trie_root.search_word(s[i:j+1]):
                    dp[i]=min(dp[i], dp[j+1])
        return dp[0]

                
        