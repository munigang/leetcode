class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        b=len(s)
        count=-1
        for i in range(b):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                 count=max(count,j-i-1)
        return count


        