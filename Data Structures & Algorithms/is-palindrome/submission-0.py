class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        c=''
        for ch in s:
            if ch.isalnum():
                c+=ch
        return c==c[len(c)-1::-1]
