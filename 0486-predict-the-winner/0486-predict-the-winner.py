class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def get_score_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            pick_left = nums[left] - get_score_diff(left + 1, right)
            pick_right = nums[right] - get_score_diff(left, right - 1)
            return max(pick_left, pick_right)
        return get_score_diff(0, len(nums) - 1) >= 0