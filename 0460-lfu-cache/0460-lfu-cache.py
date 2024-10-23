class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minf = 0
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)

    def insert(self, key: int, frequency: int, value: int):
        self.frequencies[frequency][key] = value
        self.cache[key] = (frequency, value)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        frequency, value = self.cache[key]
        del self.frequencies[frequency][key]

        if not self.frequencies[frequency]:
            del self.frequencies[frequency]
            if self.minf == frequency:
                self.minf += 1
        
        self.insert(key, frequency + 1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            self.cache[key] = (self.cache[key][0], value)
            self.get(key)
            return
        
        if len(self.cache) >= self.capacity:
            evict_key, _ = self.frequencies[self.minf].popitem(last=False)
            del self.cache[evict_key]
        
        self.minf = 1
        self.insert(key, 1, value)

