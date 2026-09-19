class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_new = ''.join(s.split(" ")).lower()
        s_new2 = ""
        for e in s:
            if e.isalnum():
                s_new2+=e.lower()
        # print(s_new2, s_new2[::-1])
        return s_new2 == s_new2[::-1] 
        # for e in s_new:
        #     if e is isalpha()