class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            left=1
            right=1
            if i==len(nums)-1:
                left=math.prod(nums[:i])
            else:
                left=math.prod(nums[:i])
            if i==len(nums)-1:
                output.append(left)
                continue
            else:
                right=math.prod(nums[i+1:])
            output.append(left*right)
        return output