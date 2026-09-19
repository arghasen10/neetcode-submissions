class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        elif nums[0] == 0:
            return False
        else:
            for i in range(1, nums[0]+1):
                if self.canJump(nums[i:]):
                    return True
                
            return False
