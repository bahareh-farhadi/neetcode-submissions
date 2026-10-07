# The idea is that we generate every possible word for each word in wordList and check if it exists in the list, if it does then we do a BFS to find the shortest path to the endWord.
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        queue=deque()
        queue.append((beginWord, 1))
        while len(queue)>0:
            elem=queue.popleft()
            word=elem[0]
            length=elem[1]
            for i in range(len(word)):
                for j in range(97, 123):
                    if ord(word[i])==j:
                        continue
                    if i+1<len(word):
                        new_word=word[:i]+chr(j)+word[i+1:]
                    else:
                        new_word=word[:i]+chr(j)
                    if new_word in wordList:
                        if new_word==endWord:
                            return length+1
                        queue.append((new_word, length+1))
                        wordList.remove(new_word)
        return 0



        
        