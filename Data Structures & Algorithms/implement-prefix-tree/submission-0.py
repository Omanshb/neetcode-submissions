class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        # Root node of the trie, which starts with an empty node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at the root of the trie
        node = self.root
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not already a child of the current node, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node
            node = node.children[char]
        
        # After inserting all characters, mark the end of the word
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Start at the root of the trie
        node = self.root
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not found, return False
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        
        # Return True if the word ends at a valid end-of-word node
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start at the root of the trie
        node = self.root
        
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not found, return False
            if char not in node.children:
                return False
            # Move to the next node
            node = node.children[char]
        
        # If all characters of the prefix are found, return True
        return True
