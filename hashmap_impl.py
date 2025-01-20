class HashMap:
    def __init__(self, max = 100):
        self.max = max
        self.array = [None for i in range(self.max)]
        self.keys = []

    def get_hash(self, key: str):
        ascii_sum = 0
        for char in key:
            ascii_sum += ord(char)
        
        return ascii_sum % self.max

    def __setitem__(self, key: str, val):
        index = self.get_hash(key)
        print("Index to save:", index)
        self.array[index] = val

        if not self.keys.__contains__(key):
            self.keys.append(key)

    def __getitem__(self, key: str):
        return self.array[self.get_hash(key)]
    
    def __delitem__(self, key: str):
        index = self.get_hash(key)
        self.array[index] = None
        self.keys.remove(key)
    
    def print_all_keys_and_values(self):
        for key in self.keys:
            print((key, self.array[self.get_hash(key)]))


map = HashMap()

map["1"] = "A"
map["2"] = "B"
map["3"] = "C"
map.print_all_keys_and_values()

map["1"] = "Z"
map.print_all_keys_and_values()
print("-"*20)

del map["1"]
map.print_all_keys_and_values()