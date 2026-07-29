import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        half_counts = {}
        mid_char = ""

        for char, count in counts.items():
            if count % 2 != 0:
                mid_char = char
            half_counts[char] = count // 2

        N = sum(half_counts.values())

        def total_perms_of(length, freqs):
            res = math.factorial(length)
            for f in freqs.values():
                res //= math.factorial(f)
            return res

        total_perms = total_perms_of(N, half_counts)
        if k > total_perms:
            return ""

        half_string_chars = []
        available_chars = sorted(half_counts.keys())
        remaining = N
        current_perms = total_perms  

        for _ in range(N):
            for char in available_chars:
                if half_counts[char] > 0:
                    perms = current_perms * half_counts[char] // remaining
                    if k <= perms:
                        half_counts[char] -= 1
                        half_string_chars.append(char)
                        remaining -= 1
                        current_perms = perms
                        break
                    else:
                        k -= perms

        half_string = "".join(half_string_chars)
        return half_string + mid_char + half_string[::-1]