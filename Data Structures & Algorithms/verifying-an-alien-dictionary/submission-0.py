class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map=dict()
        count=0
        for char in order:
            char_map[char]=count
            count+=1
        
        for i in range(1, len(words)):
            # compare the current word to the previous word
            j=0
            while j<min(len(words[i]), len(words[i-1])):
                w1=char_map[words[i-1][j]]
                w2=char_map[words[i][j]]
                if w1==w2:
                    j+=1
                elif w1<w2:
                    break
                elif w1>w2:
                    return False
            if j==min(len(words[i]), len(words[i-1])):
                # if one is the prefix of the other but the second one is a prefix of the first one
                if len(words[i-1])>len(words[i]):
                    return False
        return True


        