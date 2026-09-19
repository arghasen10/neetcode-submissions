class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]


        left_mul = [1]*len(nums)
        right_mul = [1]*len(nums)

        for i in range(1, len(nums)):
            left_mul[i] = nums[i-1]*left_mul[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_mul[i] = nums[i+1]*right_mul[i+1]
        
        final = []

        for i, j in zip(left_mul, right_mul):
            final.append(i*j)
        
        return final

