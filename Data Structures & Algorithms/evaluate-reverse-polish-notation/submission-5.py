class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        add_stack = []
        for el in tokens:
            if el not in '+-*/' and len(el) == 1:
                add_stack.append(int(el))
            else:
                if el == "+":
                    add_stack.append(add_stack.pop() + add_stack.pop())
                elif el == "-":
                    n1 = add_stack.pop()
                    n2 = add_stack.pop()
                    add_stack.append(n2-n1)
                elif el == "*":
                    add_stack.append(add_stack.pop() * add_stack.pop())
                else:
                    n1 = add_stack.pop()
                    n2 = add_stack.pop()
                    add_stack.append(n2//n1)
        return add_stack[0]