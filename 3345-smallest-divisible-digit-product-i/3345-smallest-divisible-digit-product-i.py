from math import prod
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if prod(int(digit) for digit in str(n)) % t == 0:
                return n
            n += 1