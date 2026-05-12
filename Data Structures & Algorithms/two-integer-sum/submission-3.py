class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, item in enumerate(nums):
            if target-item in nums:
                if i==nums.index(target-item):
                    continue
                else:
                    if i> nums.index(target-item):
                        return [nums.index(target-item), i]
                    else:
                        return [i, nums.index(target-item)]