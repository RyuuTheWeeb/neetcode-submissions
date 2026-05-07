class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        for i in range(l):
            c=0
            for j in range(l):
                if nums[i]==nums[j]:
                    c=c+1
            if c>1:
                return True
        return False