class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            left=math.prod(nums[:i])
            if i==len(nums)-1:
                output.append(left)
                return output
            else:
                right=math.prod(nums[i+1:])
            output.append(left*right)
        