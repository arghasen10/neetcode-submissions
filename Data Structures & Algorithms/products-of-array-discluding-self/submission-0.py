class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_sub_arr = [1]*len(nums)
        right_sub_arr = [1]*len(nums)
        for i in range(1, len(nums)):
            left_sub_arr[i] = nums[i-1]*left_sub_arr[i-1] 
        for i in range(len(nums)-2, -1, -1):
            right_sub_arr[i] = right_sub_arr[i+1]*nums[i+1]

        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = left_sub_arr[i]*right_sub_arr[i]
        return res