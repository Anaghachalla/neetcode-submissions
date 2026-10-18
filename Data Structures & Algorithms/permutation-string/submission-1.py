class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        l = 0
        s1Sorted = sorted(s1)
        for r in range(len(s1)-1, len(s2)):
            localSorted = sorted(s2[l:r+1])
            if s1Sorted == localSorted:
                return True
            l+=1
        return False

        