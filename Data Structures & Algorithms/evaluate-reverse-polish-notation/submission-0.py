class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rev_tokens = tokens[::-1]
        cur_el = int(rev_tokens.pop())
        while len(rev_tokens) > 0:
            el = int(rev_tokens.pop())
            sign = rev_tokens.pop()
            if sign == "+":
                cur_el += el
            elif sign == "-":
                cur_el -= el
            elif sign == "*":
                cur_el *= el
            else:
                cur_el = cur_el // el
        return cur_el