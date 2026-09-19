class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_new = ''.join(s.split(" ")).lower()
        s_new2 = ""
        for e in s:
            if e.isalnum():
                s_new2+=e.lower()
                # s_new2.append(e)
            # s_new = s_new.split(s_new[-1])[0]
        # s_new = ''.join(s_new2)
        print(s_new2, s_new2[::-1])
        return s_new2 == s_new2[::-1] 
        # for e in s_new:
        #     if e is isalpha()