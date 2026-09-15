class Node:
    def __init__(self):
        self.hashmap=dict()
        self.end=False
    
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, word):
        curr=self.root
        for char in word:
            if char in curr.hashmap:
                curr=curr.hashmap[char]
            else:
                new_node=Node()
                curr.hashmap[char]=new_node
                curr=new_node
        curr.end=True
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        dp=list()
        for i in range(len(s)+1):
            dp.append(0)
        for i in range(len(s)-1, -1, -1):
            # first possibility is that the current character is extra
            dp[i]=1+dp[i+1]
            curr=trie.root

            # second possibility is that the current character is found so we have to see if the rest is also found in the trie or not
            for j in range(i, len(s)):
                if s[j] not in curr.hashmap:
                    break
                else:
                    curr=curr.hashmap[s[j]]
                    if curr.end==True:
                        # if it is the end of the string and since we found the full word we can set dp[i] to dp[j+1] so whatever the min extra characters of the rest of string is would be dp[i]. 
                        dp[i]=min(dp[i], dp[j+1])
        return dp[0]

        

        