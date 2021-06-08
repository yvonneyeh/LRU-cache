# LRU cache
- A cache is like a dictionary/hashmap.
- It has 2 methods: put(key, value) and get(key)
- It also has a MAX_SIZE
- If the cache is full, remove an item before putting in an item to stay under the max size
- Which item to remove? The least recently used/accessed item.
- Implement put and get methods.

### Example with MAX_SIZE = 3
- cache = Cache(max_size=3)
- cache.put("a", 3)    // size is 1, "a" is least recent item
- cache.get("a")       // returns 3
- cache.put("b", 4)    // size is 2
- cache.put("c", 5)    // size is 3, cache is full
- cache.put("d", 6)    // evict "a", "b" is now least recent item
- cache.get("a")       // returns null ("a" is no longer in cache)
- cache.get("b")       // returns 4, "b" is now most recent item, "c" is now least recent item
- cache.put("e", 5)    // evict "c", "d" is now least recent item
