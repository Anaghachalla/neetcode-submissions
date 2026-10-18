class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        s1freq, s2freq = [0]*26, [0]*26
        for i in range(len(s1)):
            s1freq[ord(s1[i]) - ord('a')] +=1
            s2freq[ord(s2[i]) - ord('a')] +=1
        if s1freq == s2freq:
            return True
        l = 0
        for i in range(len(s1), len(s2)):
            s2freq[ord(s2[i]) - ord('a')] +=1
            s2freq[ord(s2[l]) - ord('a')] -=1
            l+=1
            if s1freq == s2freq:
                return True
        return False


