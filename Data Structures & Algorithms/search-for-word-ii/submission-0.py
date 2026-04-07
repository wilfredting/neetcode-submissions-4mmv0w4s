class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(row, col, visited, trie_node, ans):
            if row < 0 or row == len(board) or col < 0 or col == len(board[0]):
                return
            
            if (row, col) in visited:
                return
            
            if board[row][col] not in trie_node.nodes:
                return

            next_trie = trie_node.nodes[board[row][col]]
            if next_trie.word:
                ans.add(next_trie.word)

            visited.add((row, col))

            for new_row, new_col in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                dfs(new_row, new_col, visited, next_trie, ans)

            visited.remove((row, col))

        ans = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, set(), trie, ans)

        return list(ans)
        
class Trie:
    def __init__(self):
        self.nodes = {}
        self.word = None

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Trie()
            curr = curr.nodes[c]
        curr.word = word