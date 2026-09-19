class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charSet = set()
        res=0
        for r in range(len(s)): #r=3
            while s[r] in charSet: #
                charSet.remove(s[l]) #[]
                l+=1                 #2  
            charSet.add(s[r]) #["w","k"]
            res=max(res,r-l+1) #2
        return res