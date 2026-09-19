class Solution:
    def trap(self, height: List[int]) -> int:
        left_height = [0]*len(height)
        right_height = [0]*len(height)
        for i in range(1,len(height)):
            left_height[i] = max(left_height[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            right_height[i] = max(right_height[i+1],height[i+1])
        water=0
        for i in range(len(height)):
            water+=max(0, min(left_height[i],right_height[i])-height[i])
        # [0,2,0,3,1,0,1,3,2,1]
        # [0,0,2,2,3,3,3,3,3,3] 
        # [3,3,3,3,3,3,3,2,1,0]
        # [0,0,2,2,4,7,9,9,9,9]
        return water