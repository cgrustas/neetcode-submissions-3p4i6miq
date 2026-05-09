class TrieNode: 
    def __init__(self):
        self.children = {}
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert all the words into the trie
        root = TrieNode()
        for i, word in enumerate(words): 
            curr = root
            for c in word: 
                if c not in curr.children: 
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.index = i
        
        # traverse through the board 
        rows, cols = len(board), len(board[0])
        visited = set()
        res = []
        def dfs(row, col, node): 
            if node.index != -1: 
                res.append(words[node.index])
                node.index = -1
            
            # check for boundaries 
            if (row < 0 or col < 0 or row >= rows or col >= cols 
                or board[row][col] not in node.children or (row, col) in visited): 
                return
            
            visited.add((row, col))

            char = board[row][col]
            next_node = node.children[char]

            dfs(row + 1, col, next_node)
            dfs(row - 1, col, next_node)
            dfs(row, col + 1, next_node)
            dfs(row, col - 1, next_node)

            visited.remove((row, col))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children: 
                    dfs(r, c, root)
        return res