class AmortizedQueue:
    def __init__(self):
        self.queue = []
        self.move_count = 0  # Counter for move operations
        self.operation_count = 0  # Counter for total operations
        self.total_cost = 0  # To accumulate total cost

    def move_elements(self):
        # Move all elements to the front (simulate an expensive operation)
        n = len(self.queue)
        if n > 1:
            self.queue = self.queue[::-1]
        self.move_count += 1
        self.operation_count += 1
        cost = n  # Moving all elements is an O(n) operation
        self.total_cost += cost
        print(f"Move operation: Moved {n} elements. Cost: O({cost})")

    def enqueue(self, item):
        self.queue.append(item)
        self.operation_count += 1
        self.total_cost += 1  # Enqueue operation costs O(1)
        print(f"Enqueued {item}. Cost: O(1)")

    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            self.operation_count += 1
            self.total_cost += 1  # Dequeue operation costs O(1)
            print(f"Dequeued {item}. Cost: O(1)")
            return item
        else:
            print("Queue is empty.")
            return None

    def calculate_amortized_cost(self):
        amortized_cost = self.total_cost / self.operation_count if self.operation_count else 0
        print(f"Total cost: {self.total_cost}")
        print(f"Total operations: {self.operation_count}")
        print(f"Amortized cost per operation: O({amortized_cost:.2f})")

# Simulate the queue operations
queue = AmortizedQueue()

# Enqueue some elements
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')

# Perform a move operation (costly)
queue.move_elements()

# Enqueue and dequeue a few elements
queue.enqueue('D')
queue.dequeue()

# Perform another move operation (costly)
queue.move_elements()

# Calculate the amortized cost
queue.calculate_amortized_cost()
