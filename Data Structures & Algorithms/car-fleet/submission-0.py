class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_p_s = [[p, s] for p, s in zip (position, speed)]
        pair_p_s = sorted(pair_p_s)
        stack = []        
        for p, s in pair_p_s[::-1]:
            time_to_reach = (target-p)/s
            stack.append(time_to_reach)
            while len(stack) >=2 and stack [-1] <= stack[-2]:
                stack.pop()
        return len(stack)