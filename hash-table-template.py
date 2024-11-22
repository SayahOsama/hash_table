class HashTable:
    def __init__(self,size):
        self.hash_table = []
        for _ in range(size):
            self.hash_table.append([])
        self.size = size
        
    def _hash_function(self,key):
        return key%self.size
    
    def get(self, key):
        index = self._hash_function(key)
        for k, v in self.hash_table[index]:
            if k == key:
                return v
        return None  # Key not found
        

    def set(self, key, value):
        index = self._hash_function(key)
        # Check if the key already exists in the chain
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:
                self.hash_table[index][i] = (key, value)  # Update value
                return
        # If key does not exist, append the key-value pair
        self.hash_table[index].append((key, value))

# Example usage
table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: good (because 123 overwrote the value at index 3)
print(table.get(5251))  # Output: world
print(table.get(22))    # Output: None (no value at 22 % 5 = 2)

