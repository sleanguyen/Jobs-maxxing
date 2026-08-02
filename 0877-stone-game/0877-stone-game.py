from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def get_score_diff(left: int, right: int) -> int:
            if left == right:
                return piles[left]
            pick_left = piles[left] - get_score_diff(left + 1, right)
            pick_right = piles[right] - get_score_diff(left, right - 1)
            return max(pick_left, pick_right)
        return get_score_diff(0, len(piles) - 1) > 0