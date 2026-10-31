class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        total = sum(nums)
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
                break
            left += nums[i]
        return -1
