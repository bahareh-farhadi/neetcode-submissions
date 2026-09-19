# we use backtracking for this.
# we have to do a dfs on all elements. we make a choice on a valid element, we do dfs on its neighbours, and then we undo the choice at the end

# TIME COMPLEXITY: O(m*n*4^L) where m and n are board dimensions since "exist" function explores every single element. and the "dfs" function looks at 4 directions each time and each direction can span the full length of word which is L so it is 4^L
# SPACE COMPLEXITY: O(L) since visited will hold at most L items each time
class Solution:
    visited=set()
    def dfs(self, board, word, word_index, row, col):
        if word_index==len(word):
            # have found all letters in the word
            return True
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
            return False
        if (row, col) in Solution.visited:
            return False
        if board[row][col]!=word[word_index]:
            # not a valid choice
            return False
        
        # make the choice
        Solution.visited.add((row,col))

        res=self.dfs(board, word, word_index+1, row+1, col) or self.dfs(board, word, word_index+1, row, col+1) or self.dfs(board, word, word_index+1, row-1, col) or self.dfs(board, word, word_index+1, row, col-1)
        # undo the choice
        Solution.visited.remove((row, col))

        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        Solution.visited.clear()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j)==True:
                    return True
        
        return False


        