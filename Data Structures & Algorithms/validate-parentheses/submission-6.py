class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeTheOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c not in closeTheOpen:
                stack.append(c)   
            else:
                if stack and stack[-1] == closeTheOpen[c]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False