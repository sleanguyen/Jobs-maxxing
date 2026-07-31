from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = Counter(word)
        sorted_freqs = sorted(freq_map.values(), reverse=True)
        total_pushes = 0
        for i, freq in enumerate(sorted_freqs):
            pushes_per_char = (i//8) + 1
            total_pushes += freq * pushes_per_char
        return total_pushes
        