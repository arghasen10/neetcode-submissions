class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}

        for i, e in enumerate(nums):
            if (target-e) not in mem:
                mem[e] = i
            else:
                return [mem[target-e], i]