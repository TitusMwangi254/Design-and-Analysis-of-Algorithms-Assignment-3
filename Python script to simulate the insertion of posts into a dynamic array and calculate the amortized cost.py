class DynamicArray:
    def __init__(self):
        self.array = [None]  # Initial array with size 1
        self.size = 0        # Number of elements
        self.capacity = 1    # Maximum capacity of the array

    def insert(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        # Double the capacity and copy existing elements
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return str(self.array[:self.size])

# Example usage
posts = DynamicArray()
for i in range(1, 9):
    posts.insert(f"Post {i}")
    print(f"After inserting: {posts}")
