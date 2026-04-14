class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[::-1]# to create equation with brackets to solve straight forward?

# How many signs more than 2 in a line can be? two is okay 3 is over
# let it be two max
# if it is i only store this extra sign

# put the value you calculated in stack. why? i  will go through stack second time? for time complexety
# i cant reach deep values in stack then or here put value in extra stack but it will be reversed equation


 #(3 + 4) × (5 + 6) becomes 3 4 + 5 6 + × 
 
        cur_el = int(tokens.pop())
        while len(tokens) > 0:
            if tokens[-1] not in '+-*/':
                el = int(tokens.pop())
            else:
                sign = tokens.pop()
                el = int(tokens.pop())
            if tokens[-1] in '+-*/':    
                sign = tokens.pop()
            else:
                tokens.append(cur_el)
                cur_el = int(tokens.pop())
                el = int(tokens.pop())
                sign = tokens.pop()
            if sign == "+":
                cur_el += el
            elif sign == "-":
                cur_el -= el
            elif sign == "*":
                cur_el *= el
            else:
                cur_el = cur_el // el
        return cur_el