class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        i = 0
        nums = sorted(nums)
        for i, elem in enumerate(nums):
            if i>0 and elem == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                targetSum = elem + nums[l] + nums[r]
                if targetSum > 0:
                    r-=1
                elif targetSum <0:
                    l+=1
                else:
                    triplets.append([elem, nums[l], nums[r]])  #[[-1,0,1]]
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return triplets

        # [-4]    -> 1   [-1,0,1], [-1, 2, -1]
        # S = {0:1, 1:1, 2:1, -1:1,-4:0 }
