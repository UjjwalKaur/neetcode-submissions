class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:

    # create a hash map that stores nodes as values
    # nodes are linked together as doubly linked lists for insertion, deletion according to use

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # dummy nodes
        # left = LRU, right = Most Recently Used
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # connect the two pointers
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        # get the value if node exists in the cache
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # removing node if it already exists
        if key in self.cache:
            self.remove(self.cache[key])
        # reinserting with the changed value
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        # deleting least recently used node if it exceeds capacity
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
