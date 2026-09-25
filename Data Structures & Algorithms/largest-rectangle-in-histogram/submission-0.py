class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # {index, height}
        max_area = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1]>height:
                previous_start, previous_height = stack.pop()
                max_area = max(max_area, previous_height*(index-previous_start))
                start = previous_start
            stack.append((start,height))
        for start, height in stack:
            max_area = max(max_area, height*(len(heights)-start))
        return max_area