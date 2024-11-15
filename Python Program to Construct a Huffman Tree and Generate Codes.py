import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    # Create a priority queue
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the tree

def generate_huffman_codes(node, prefix="", codebook={}):
    if node is None:
        return
    if node.char is not None:  # Leaf node
        codebook[node.char] = prefix
    generate_huffman_codes(node.left, prefix + "0", codebook)
    generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

# Example usage
if __name__ == "__main__":
    # Character frequencies
    text = "AAABBCDDDDEEEFFFF"
    frequencies = Counter(text)

    # Build Huffman tree
    root = build_huffman_tree(frequencies)

    # Generate Huffman codes
    codes = generate_huffman_codes(root)
    print("Huffman Codes:", codes)

    # Encode the text
    encoded_text = ''.join(codes[char] for char in text)
    print("Encoded Text:", encoded_text)
