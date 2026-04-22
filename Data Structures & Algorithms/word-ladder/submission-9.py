class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        adj = {}

        for word in wordList:
            adj[word] = []
            for w in wordList:
                diff = 0
                for c in range(len(w)):
                    if word[c] != w[c]:
                        diff +=1
                        if diff > 1:
                            break
                if diff == 1:
                    adj[word].append(w)
        
        queue = deque([beginWord])
        level = 1
        while level < len(wordList) + 1:
            length = len(queue)
            for i in range(length):
                w = queue.popleft()
                if w == endWord:
                    return level
                for nei in adj[w]:
                    queue.append(nei)

            level += 1
        return 0
