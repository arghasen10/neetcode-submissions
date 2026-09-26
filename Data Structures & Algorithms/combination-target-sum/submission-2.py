class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        combinations = []
        def backtrack(start, remaining):
            # print(results)
            if remaining == 0:
                results.append(combinations.copy())
                return
            for i in range(start, len(nums)):
                value = nums[i]
                if value > remaining:
                    continue
                # remaining = target-value
                combinations.append(value)
                backtrack(i, remaining-value)
                combinations.pop()


        
        backtrack(0, target)
        return results
                    
