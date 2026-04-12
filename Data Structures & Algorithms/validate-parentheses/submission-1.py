class Solution:
    def isValid(self, s: str) -> bool:
        # push l.append(2)
        # peek l[-1]
        # pop l.pop()
        # last in first out - lifo
        #s_dict = {}
        #l = list(s)
        #l.pop()
        #brute fore
        if not s:
            return False
        l = list(s)
        for i in range(0,len(l)//2):
            for j in range(len(l) - 1,len(l)//2 - 1):
                if l[i] == l[j]:
                    continue
                else:
                    return False
        return True