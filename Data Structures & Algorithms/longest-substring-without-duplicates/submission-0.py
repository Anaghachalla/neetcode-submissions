class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s)==1:
            return len(s)
        l,r = 0,1
        seen = defaultdict(int)
        seen[s[l]] = 0
        maxLen = 0
        while(r<len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    del seen[s[l]]
                    l+=1
            else:
                maxLen = max(maxLen, (r-l+1))
                seen[s[r]] += 1
                r+=1
        return maxLen


        