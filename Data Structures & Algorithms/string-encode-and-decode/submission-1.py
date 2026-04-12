class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = ''
        for word in strs:
            s += str(len(word)) + "#" + word
            for alpha in word:
               s += str(ord(alpha)) + str(ord("."))
            if len(strs) - 1 != ind:
                s += str(ord(","))
        return s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        l, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            l.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return l






            