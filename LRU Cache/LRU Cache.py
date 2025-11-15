class ListNode:
    def __init__(self, key: int, value: int, next: Optional[ListNode] = None, prev: Optional[ListNode] = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # value to its node memory reference
        self.head = ListNode(-1, -1)
        self.cap = capacity
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            # add as most recently used
            node = self.cache[key]

            self.remove(node)
            self.add(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache[key]
            self.remove(old)

        new_node = ListNode(key, value)
        self.cache[key] = new_node

        self.add(new_node)

        if len(self.cache) > self.cap:
            # evict
            lru = self.head.next

            if lru:
                self.remove(lru)

            del self.cache[lru.key]


    def add(self, node):
        tail_last = self.tail.prev
        tail_last.next = node
        node.prev = tail_last
        node.next = self.tail
        self.tail.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)