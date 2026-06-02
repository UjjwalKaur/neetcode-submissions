class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:   
            if c == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2)
            elif c == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif c == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 * op1)
            elif c == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(float(op2) / op1))
            else:
                stack.append(int(c))

        return stack[0]

        