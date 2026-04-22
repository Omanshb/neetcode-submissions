class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        oldNode = self.hashmap[key]
        self.remove(oldNode)
        newNode = self.add(key, self.hashmap[key].value)
        self.hashmap[key] = newNode
        return self.hashmap[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            oldNode = self.hashmap.pop(key)
            self.remove(oldNode)

        if len(self.hashmap) == self.capacity:
            self.hashmap.pop(self.left.next.key)
            self.remove(self.left.next)
        
        newNode = self.add(key, value)
        self.hashmap[key] = newNode
        print(self.hashmap)
        
    def add(self, key, value):
        new = Node(key, value)
        new.prev = self.right.prev
        self.right.prev.next = new
        new.next = self.right
        self.right.prev = new
        return new
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
