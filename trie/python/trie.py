class Node:
    def __init__(self, value = None):
        self.value = value
        self.nodes = [Node] * 26

class Trie:
    def __init__(self):
        self.nodes = [Node()] * 26

    def exists(self, string: str):
        curr = self.nodes
        for i in range(0, len(string)):
            if curr[ord(string[i]) - 97].value != None:
                curr = curr[ord(string[i]) - 97].nodes
            else:
                return False
        return True
    
    def insert(self, string: str):
        curr = self.nodes
        for char in string:
            curr[ord(char) - 97] =  Node(char)
            curr = curr[ord(char) - 97].nodes