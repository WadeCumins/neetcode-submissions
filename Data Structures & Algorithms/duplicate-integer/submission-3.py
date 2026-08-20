class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = set(nums)
        if len(dedup) == len(nums):
            return False
        else:
            return True
        