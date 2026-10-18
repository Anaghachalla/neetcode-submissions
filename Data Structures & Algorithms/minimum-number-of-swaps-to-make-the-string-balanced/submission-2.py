class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        maxCount = 0
        for br in s:
            if br == "]":
                count+=1
                maxCount = max(count, maxCount)
            else:
                count-=1
        return (maxCount + 1) // 2