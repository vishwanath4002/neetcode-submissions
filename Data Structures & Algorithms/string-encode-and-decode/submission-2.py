class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + '#' + i
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            word = ""
            num = 0
            while s[i] != '#':
                num = num*10 + int(s[i])
                i += 1
            
            i += 1
            for j in range(num):
                word += s[i]
                i += 1
            
            res.append(word)
            word = ""
            num = 0

        return res
 



