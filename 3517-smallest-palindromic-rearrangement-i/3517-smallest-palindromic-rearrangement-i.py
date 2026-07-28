from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count= Counter(s)
        left_half =[]
        mid = ""
        for char in sorted(count.keys()):
            if count[char] % 2 != 0:
                mid = char
            left_half.append(char*(count[char] // 2))
        left_str = "".join(left_half) 
        return left_str + mid + left_str[::-1]