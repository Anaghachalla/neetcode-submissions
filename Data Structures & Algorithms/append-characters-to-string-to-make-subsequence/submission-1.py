class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        trem = len(t)
        a,b = 0,0
        while (a < len(s) and b < len(t)):
            if s[a] == t[b]:
                trem-=1
                a+=1
                b+=1
            else:
                a+=1
            if trem ==0:
                return 0
        return trem
            

        