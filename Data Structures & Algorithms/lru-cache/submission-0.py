class LRUCache:

    def __init__(self, capacity: int):
        self.h = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        self.h[key] = self.h.pop(key) # pop to remove from h then add it back
        # now MRU is at the end of h, since dict preserves insertion order
        return self.h[key]

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h.pop(key)
        elif len(self.h) == self.capacity: 
            del self.h[next(iter(self.h))]
        self.h[key] = value
        
