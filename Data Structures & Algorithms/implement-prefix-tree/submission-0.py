class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.nodes[ord(c) - ord('a')]:
                curr.nodes[ord(c) - ord('a')] = TrieNode()
            curr = curr.nodes[ord(c) - ord('a')]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            curr = curr.nodes[ord(c) - ord('a')]
            if not curr:
                return False
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            curr = curr.nodes[ord(c) - ord('a')]
            if not curr:
                return False
        return True
        