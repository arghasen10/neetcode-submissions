class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        left, right = 0,len(heights)-1
        while left<right:
            max_val = max(max_val, min(heights[left], heights[right])*(right-left)) 
            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         store = min(heights[i], heights[j])*(j-i)
        #         if store > max_val:
        #             max_val = store
        return max_val
