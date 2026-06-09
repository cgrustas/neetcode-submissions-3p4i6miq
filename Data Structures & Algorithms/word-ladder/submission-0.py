class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '*' + word[i + 1:]
                adj_list[wildcard].append(word)
        
        def bfs():            
            q = collections.deque([(beginWord, 1)])
            visit = set([beginWord])

            while q:
                currentWord, steps = q.popleft()
                if currentWord == endWord:
                    return steps
                        
                for i in range(len(currentWord)):
                    wildcard = currentWord[:i] + '*' + currentWord[i + 1:]
                    for neighboringWord in adj_list[wildcard]:
                        if neighboringWord in visit:
                            continue
    
                        q.append((neighboringWord, steps + 1))
                        visit.add(neighboringWord)

            return 0
            
            
        return bfs()