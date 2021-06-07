# implementation with dictionary
class Cache1:
  max_size = 3
  current_size = 0

  def __init__(self, dict):
  	self.dict = dict

    keys = dict.keys()

    if len(keys) > self.max_size:
    	dict

  def put(self, item, value):
  	self.current_size += 1
    self.dict[self.item] = value

  def get(self, item):
    return self.dict[item]


# implementation with linked list
class Cache2:
	max_size = 3
  current_size = 0

  def __init__(self, llist):
  	self.llist = llist


  def put(self, item, value):

  	if len(llist) > self.max_size:
    	self.llist.pop(0)
      self.current_size -= 1


    self.llist.enqueue(item)
    self.llist[item].add(value)
    self.current_size += 1


  def get(self, item):

  	if item not in self.llist:
    	reutn null

    if self.llist[item].node is not None:
    	return node


cache.put("a", 3)    // [a]
cache.get("a")       // 3
cache.put("b", 4)    // [a, b]
cache.put("c", 5)    // [a, b, c]
cache.put("d", 6)    // [b, c] > [b, c, d]
cache.get("a")       // null
cache.get("b")       // 4
cache.put("e", 5)    // [c, d] > [c, d, e]


store a counter for when you access an item
when removing an item loop through the items in the linked list to check the read state and remove the item with the oldest read state
