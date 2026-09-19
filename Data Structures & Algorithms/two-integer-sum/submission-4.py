class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            val = (target-num)
            if val in nums[i+1:]:
                 return [i,nums[i+1:].index(val)+i+1]
        
