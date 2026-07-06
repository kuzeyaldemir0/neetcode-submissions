class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Input: s = "([{}])"
        # If it's a left bracket we want to push
        # if it's right, we want to peek and pop if match
        
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            elif p == ")" or p == "]" or p == "}":
                if len(stack) == 0: return False
                top_el = stack[-1]
                if (top_el == "(" and p == ")") or (top_el == "[" and p == "]") or (top_el == "{" and p == "}"):
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) != 0: return False
        return True