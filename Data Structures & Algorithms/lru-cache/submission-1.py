class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        self.mp = {}
    
    def insert(self, curr):
        prev = self.right.prev
        next = self.right

        prev.next = curr
        curr.prev = prev

        next.prev = curr
        curr.next = next
    
    def remove(self, curr: Node):
        prev = curr.prev
        next = curr.next

        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        newNode = Node(key, value)
        self.insert(newNode)
        self.mp[key] = newNode

        if len(self.mp) > self.capacity:
            rem = self.left.next
            self.remove(rem)
            del self.mp[rem.key]
        

