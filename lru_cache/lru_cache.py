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
    
    def __repr__(self):
        return f'CACHE: {self.cache}'

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # we first check if the key is in the cache
        if key in self.cache:
            # if it is we hold the key in a variable
            node = self.cache[key]
            # we move the key to the front of the cache
            self.storage.move_to_front(node)
            # and we return the value
            return node.value[1]
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
        # first we check if the key is in the cache
        if key in self.cache.keys():
            # if it does, we trap the node in a variable
            node = self.cache[key]
            # we update it's value to be the key/value paired passed in as a parameter
            node.value = (key, value)
            # we move the given node to the front
            self.storage.move_to_front(node)
            # we return to get out of the if statement
            return
        # we need to check if cache is at max capacity
        if self.size == self.limit:
            # so we first delete the node from the cache
            del self.cache[self.storage.tail.value[0]]
            # we then remove that last item on our LL as well
            self.storage.remove_from_tail()
            # we need to manually take care of our cache size as we add and delete
            self.size -= 1
        # we add the new node to the head of our LL
        self.storage.add_to_head((key, value))
        # we need to set our new node to be the new head
        self.cache[key] = self.storage.head
        # increase size by 1
        self.size += 1

# if __name__ == '__main__':
#     lru_cache = LRUCache(3)
#     lru_cache.set('item1', 'a')
#     lru_cache.set('item2', 'b')
#     lru_cache.set('item3', 'c')
#     lru_cache.set('item4', 'g')
#     print(lru_cache.get('item2'))
#     print(lru_cache)


        
