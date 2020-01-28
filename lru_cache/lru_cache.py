from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.cache = {}
        self.limit = limit
        self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        print('In CACHE from GET', self.cache.keys())
        #check if key is in cache
        if key in self.cache:
            #grabs the node in a variable (easier read)
            node = self.cache[key]
            #moves the target to the tail of our storage
            self.storage.move_to_end(node)
            #returns the value of the node
            print('TAIL', self.storage.tail.value[0])
            return node.value[1]
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        print('In CACHE', self.cache)
        #checks of key exists in cache
        if key in self.cache:
            #grabs exisiting key in cache
            node = self.cache[key]
            #replaces exisiting key value with current (overwrites)
            node.value = (key, value)
            #moves overwritten node to the end of the linked list (our tail)
            self.storage.move_to_end(node)
            return
        #checks if LL reached it's limit in length 
        if self.size == self.limit:
            #if it did, deletes the last node used in cache (the head)
            del self.cache[self.storage.head.value[0]]
            #deletes it also from the storage
            self.storage.remove_from_head()
            #decreases cache length manually by 1
            self.size -= 1
        #if the LL size is NOT equal to limit, adds the node to the tail of LL
        self.storage.add_to_tail((key, value))
        #sets the cache key to be equal to the storage's tail
        self.cache[key] = self.storage.tail
        #increases size by 1
        self.size += 1

       



        
