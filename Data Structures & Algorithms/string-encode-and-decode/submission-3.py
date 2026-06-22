class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strings = []
        for string in strs:
            new_strings.append(str(len(string)) + "#" + string)
        return "".join(new_strings)



    def decode(self, s: str) -> List[str]:
        res = []
        count = ""
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                count += s[i]
                i += 1
            elif s[i] == "#":
                i += 1
                str_len = int(count)
                new_str = ""
                new_str = s[i:str_len+i]
                i += str_len
                res.append(new_str)
                count = ""
        return res