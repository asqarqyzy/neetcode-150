class Solution:
    def isValid(self, s: str) -> bool:
        # push l.append(2)
        # peek l[-1]
        # pop l.pop()
        # last in first out - lifo
        #s_dict = {}
        #l = list(s)
        #l.pop()
        #brute force
        if len(s) <= 1:
            return False
        l = list()
        for i, el in enumerate(s):
            if s[i] in '([{':
                l.append(s[i])
            elif len(l) > 0:
                if s[i] == ')':
                    if l.pop() == '(':
                        continue
                    else:
                        return False
                if s[i] == '}':
                    if l.pop() == '{':
                        continue
                    else:
                        return False
                if s[i] == ']':
                    if l.pop() == '[':
                        continue
                    else:
                        return False
            else:
                return False
        return True