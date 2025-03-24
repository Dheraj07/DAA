import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def generate_huffman_codes(root, prefix="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = prefix

    generate_huffman_codes(root.left, prefix + "0", codes)
    generate_huffman_codes(root.right, prefix + "1", codes)

def huffman_coding(characters, frequencies):
    min_heap = [HuffmanNode(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(min_heap, merged)

    root = min_heap[0]
    codes = {}
    generate_huffman_codes(root, "", codes)
    return codes

characters = ['F', 'G', 'H', 'I', 'J']
frequencies = [2, 7, 24, 14, 10]

huffman_codes = huffman_coding(characters, frequencies)
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
