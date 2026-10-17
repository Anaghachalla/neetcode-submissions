class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxwater = 0
        while(l<r):
            ar = (r-l)*min(heights[l], heights[r])
            maxwater = max(ar, maxwater)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxwater


        