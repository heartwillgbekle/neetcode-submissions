class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for brac in s:
            if stack and brac in pairs :
                if stack[-1] == pairs[brac]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(brac)

        return not stack
        