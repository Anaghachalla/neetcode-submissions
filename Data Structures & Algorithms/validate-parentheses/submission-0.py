class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for i in s:
            if i not in bracket:
                stack.append(i)
            elif len(stack)>0 and bracket[i] == stack.pop():
                continue
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False