class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        total = sum(nums)
        ans = -1
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                ans = i
                break
            left += nums[i]
        return ans
