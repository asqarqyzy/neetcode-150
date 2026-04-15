class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        add_stack = []
        for el in tokens:
            if el == "+":
                add_stack.append(add_stack.pop() + add_stack.pop())
            elif el == "-":
                n1,n2 = add_stack.pop(), add_stack.pop()
                add_stack.append(n2-n1)
            elif el == "*":
                add_stack.append(add_stack.pop() * add_stack.pop())
            elif el == "/":
                n1,n2 = add_stack.pop(), add_stack.pop()
                add_stack.append(int(float(n2)/n1))
            else:
                add_stack.append(int(el))
        return add_stack[0]