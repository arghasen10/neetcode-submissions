class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ""
        for e in s:
            if e.isalnum():
                s_new+=e
        if s_new == s_new[::-1]:
            return True
        return False
