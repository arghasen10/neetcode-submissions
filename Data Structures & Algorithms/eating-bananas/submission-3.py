import math
class Solution:
   def minEatingSpeed(self, piles: List[int], h: int) -> int:
       if h == len(piles):
           return max(piles)
       if h == sum(piles):
           return 1
       # piles= sorted(piles)
       l,r=1,max(piles)
       min_val = r
       while l<=r:
           m = (l+r)//2
           sum_val = 0
           for e in piles:
               sum_val += math.ceil(e/m) #+ (1 if e%m>0)
           if sum_val > h:
               l=m+1
           if sum_val <= h:
               min_val = min(min_val,m)
               r=m-1
       return min_val
