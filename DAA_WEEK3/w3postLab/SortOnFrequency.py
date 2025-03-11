from collections import Counter

def custom_sort(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))
    return ''.join(char * freq[char] for char in sorted_chars)


strings = ["aaabbc", "aabbcc"]

for s in strings:
    print(custom_sort(s))
