class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if m in d:
                return [d[m], i]
            else:
                d[nums[i]] = i