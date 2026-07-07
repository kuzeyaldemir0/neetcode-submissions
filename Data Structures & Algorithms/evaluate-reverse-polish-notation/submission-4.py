class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number, push; if operand, double pop, calculate, and
        # push the result 
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "/" and token != "*":
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "-":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left - right)
                else:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left / right))
        return stack.pop()