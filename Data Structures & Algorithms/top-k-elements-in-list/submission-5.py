class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        listoflist = [[] for i in range(len(nums)+1)]
        
        for ele in nums:
            vals[ele] = 1 + vals.get(ele, 0)
        for key, value in vals.items():
            listoflist[value].append(key)
        output = []
        for i in range(len(listoflist)-1,0,-1):
            for j in listoflist[i]:
                output.append(j)
                if len(output) == k:
                    # break
                    return output