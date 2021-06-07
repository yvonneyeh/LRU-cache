# Class for a Doubly Linked List Node
class DLLNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

# LRU Cache class
class Cache:

    def __init__(self, MAX_SIZE):
        # MAX_SIZE:  max capactity of cache
        # Intialize all variables
        self.MAX_SIZE = MAX_SIZE
        self.map = {}
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    # This method works in O(1)
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            result = node.value
            self.delete_node(node)
            self.add_to_head(node)
            print(f'Got the value: {result} for the key: {key}')
            return result
        print(f'Did not get any value for the key: {key}')
        return -1

    # This method works in O(1)
    def put(self, key, value):
        print(f'Setting (key, value) : ({key}, {value})')
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.delete_node(node)
            self.add_to_head(node)
        else:
            node = DLLNode(key, value)
            self.map[key] = node
            if self.count < self.MAX_SIZE:
                self.count += 1
                self.add_to_head(node)
            else:
                del self.map[self.tail.prev.key]
                self.delete_node(self.tail.prev)
                self.add_to_head(node)


if __name__ == '__main__':
    # Example with MAX_SIZE = 3
    print('Testing the LRU Cache Implementation')
    cache = Cache(3)

    # store a key "a" with value 3 in the cache.
    cache.put("a", 3)    # size is 1, "a" is least recent item

    cache.get("a")       # returns 3

    # store a key "b" with value 4 in the cache.
    cache.put("b", 4)    # size is 2

    # store a key "c" with value 5 in the cache.
    cache.put("c", 5)    # size is 3, cache is full

    # evicts key "a" and store a key "d" with value 6 in the cache.
    cache.put("d", 6)    # evict "a", "b" is now least recent item

    cache.get("a")       # returns null ("a" is no longer in cache)

    cache.get("b")       # returns 4, "b" is now most recent item, "c" is now least recent item

    cache.put("e", 5)    # evict "c", "d" is now least recent item
