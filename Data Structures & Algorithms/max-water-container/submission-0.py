class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                store = min(heights[i], heights[j])*(j-i)
                if store > max_val:
                    max_val = store
        return max_val
