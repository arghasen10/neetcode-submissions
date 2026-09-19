# [1,7,2,5,4,7,3,6]
# []



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = (r-l) *min(heights[l], heights[r])
            max_val = max(max_val, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_val