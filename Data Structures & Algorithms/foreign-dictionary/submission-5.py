from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # FIX 4: removed the len(words) == 1 special case

        all_letters = {c for w in words for c in w}
        # use topological sort
        ad_list = dict() # key: letter, val: set of letters that come after it
        indegree = dict() # key: letter, val: number of nodes that come before it
        for i in range(1, len(words)):
            # prev_word counter
            k = 0
            # curr_word counter
            j = 0
            found = False                                        # FIX 2: track if a difference was found
            while j < len(words[i]) and k < len(words[i-1]):
                if words[i-1][k] != words[i][j]:                 # FIX 1: only where the letters differ
                    if words[i-1][k] not in ad_list:
                        ad_list[words[i-1][k]] = set()
                    if words[i][j] not in ad_list[words[i-1][k]]:   # FIX 1: count each edge once
                        if words[i][j] in indegree:
                            indegree[words[i][j]]+=1
                        else:
                            indegree[words[i][j]] = 1
                        ad_list[words[i-1][k]].add(words[i][j])
                    found = True
                    break                                        # FIX 1: only the first difference matters
                j+=1
                k+=1
            if not found and len(words[i-1]) > len(words[i]):    # FIX 2: longer word before its prefix
                return ""

        for letter in all_letters:
            if letter not in ad_list:
                ad_list[letter] = set()
            if letter not in indegree:
                indegree[letter] = 0
        res = ""

        queue = deque()
        for key, val in indegree.items():
            if val == 0:
                queue.append(key)
        while queue:
            letter = queue.popleft()
            res+=letter
            # FIX 3: removed all_letters.remove(letter)
            for next_letter in ad_list[letter]:
                indegree[next_letter]-=1
                if indegree[next_letter] == 0:
                    queue.append(next_letter)
        # FIX 3: removed the loop that added leftover letters
        return res if len(res) == len(indegree) else ""