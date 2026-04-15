class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        add_stack = []
        for el in tokens:
            if el not in '+-*/':
                add_stack.append(int(el))
            else:
                if el == "+":
                    add_stack.append(add_stack.pop() + add_stack.pop())
                elif el == "-":
                    add_stack.append(add_stack.pop() - add_stack.pop())
                elif el == "*":
                    add_stack.append(add_stack.pop() * add_stack.pop())
                else:
                    add_stack.append(add_stack.pop() // add_stack.pop())
        return add_stack[0]