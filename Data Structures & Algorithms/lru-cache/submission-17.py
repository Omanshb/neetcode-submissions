class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = None
        self.right = None
    
    def addNode(self, Node):
        if not self.right:
            self.left = Node
            self.right = Node
            self.cache[Node.key] = Node
            return
        
        self.right.next = Node
        Node.prev = self.right
        self.right = Node
        self.cache[Node.key] = Node
    
    def removeNode(self, Node):
        if Node.prev:
            Node.prev.next = Node.next
        if Node.next:
            Node.next.prev = Node.prev
        if Node == self.left:
            self.left = self.left.next
        if Node == self.right:
            self.right = self.right.prev
        
        self.cache.pop(Node.key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        new = Node(key, self.cache[key].value)
        self.removeNode(self.cache[key])
        self.addNode(new)
        
        return self.cache[key].value
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        
        while len(self.cache) >= self.capacity:
            self.removeNode(self.left)
        
        new = Node(key, value)
        self.addNode(new)
