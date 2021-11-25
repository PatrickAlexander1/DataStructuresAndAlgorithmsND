
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        assert(type(capacity) == int and capacity > 0)
        self.capacity = capacity
        self.items = {}
        self.n_items = 0
        self.most_recent = None
        self.recent_items = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.items:
            return -1
        else:
            # make changes to self.most_recent and self.recent_items if necessary
            if self.most_recent != key:

                self.recent_items.remove(key)
                self.recent_items.append(key)
                self.most_recent = key
            return self.items[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item. 
        if key not in self.items:
            if self.n_items < self.capacity:
                self.items[key] = value
                self.most_recent = key
                self.recent_items.append(key)
                self.n_items += 1
            else:
                # since the cache is at capacity the oldest item gets removed from the recent items
                # the oldest item also gets removed from the dictionary self.items
                removed = self.recent_items[0]
                self.recent_items = self.recent_items[1:]
                self.recent_items.append(key)
                del self.items[removed]
                self.most_recent = key
                self.items[key] = value
            
        else:
            
            if self.most_recent != key:
                self.recent_items.remove(key)
                self.recent_items.append(key)
                self.most_recent = key
                self.items[key] = value
            else:
                self.items[key] = value

# Test Case 1
print("Test Case 1:")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Test Case 2

print("Test Case 2:")
our_cache = LRU_Cache(1000)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))       # returns -1

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))       # returns 3

# Test Case 3
#print("Test Case 3:")
#our_cache = LRU_Cache(-1) # Assertion error due to capacity at less than 1
