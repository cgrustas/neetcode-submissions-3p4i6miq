class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word: 
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = PrefixTree()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
        