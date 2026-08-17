class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word        

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
        res = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, node, visited):
            char = board[row][col]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                res.add(next_node.word)


            visited.add((row,col))
            for row2, col2 in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                if min(row2, col2) < 0 or row2 >= ROWS or col2 >= COLS or (row2,col2) in visited:
                    continue
                dfs(row2, col2, next_node, visited)
            
            visited.remove((row,col))
        

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, self.root, set())

        return list(res)