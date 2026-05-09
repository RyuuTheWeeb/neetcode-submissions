class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            a=0
            b=0
            for j in range(len(s)):
                if s[i]==s[j]:
                    a=a+1
                if s[i]==t[j]:
                    b=b+1
            if a!=b:
                return False
        return True