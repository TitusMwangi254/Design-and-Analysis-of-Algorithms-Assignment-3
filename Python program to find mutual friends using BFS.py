from collections import deque

class SocialNetwork:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()

    def add_friendship(self, user1, user2):
        self.add_user(user1)
        self.add_user(user2)
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def bfs(self, start_user):
        """Perform BFS to find all friends of a user."""
        visited = set()
        queue = deque([start_user])
        friends = set()

        while queue:
            user = queue.popleft()
            if user not in visited:
                visited.add(user)
                friends.update(self.graph[user])
                queue.extend(self.graph[user] - visited)

        return friends

    def find_mutual_friends(self, user1, user2):
        """Find mutual friends between two users."""
        friends_user1 = self.bfs(user1)
        friends_user2 = self.bfs(user2)
        return friends_user1.intersection(friends_user2)

# Example usage
network = SocialNetwork()
network.add_friendship("Alice", "Bob")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Bob", "Charlie")
network.add_friendship("Bob", "David")
network.add_friendship("Charlie", "Eve")
network.add_friendship("David", "Eve")

# Find mutual friends between Alice and Bob
mutual_friends = network.find_mutual_friends("Alice", "Bob")
print("Mutual Friends:", mutual_friends)
