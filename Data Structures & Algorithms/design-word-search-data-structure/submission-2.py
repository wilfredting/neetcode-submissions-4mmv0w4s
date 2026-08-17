class WordNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        return self.__search__(word, self.root)
        
    def __search__(self, word: str, curr: WordNode) -> bool:
        for index, c in enumerate(word):
            if c == '.':
                for node in curr.children.values():
                    if self.__search__(word[index+1:], node):
                        return True
                return False
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
