class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = None # End


    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
    
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
            
        return True
