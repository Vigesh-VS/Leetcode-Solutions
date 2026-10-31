class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        output = []
        for x in nums:
            total += x
            output.append(total)
        return(output)
