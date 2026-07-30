class Solution:
    def minimumPushes(self, word: str) -> int:
        N = len(word)
        total = 0
        for i in range(N):
            total +=(i//8)+1
        return total
