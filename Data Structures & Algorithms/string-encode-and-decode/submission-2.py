class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for string in strs:
            new_string = new_string + str(len(string)) + "#" + string
        return new_string



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
                # 5#Hello5#World 
                # i = 0: count = 5
                # i = 1 -> i = 2: s[2:7] 2, 3, 4, 5, 6
                # i = 7
                new_str = s[i:str_len+i]
                i += str_len
                res.append(new_str)
                count = ""
        return res