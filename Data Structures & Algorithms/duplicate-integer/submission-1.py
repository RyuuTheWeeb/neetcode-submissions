class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    c=c+1
            if c>1:
                return True
        return False