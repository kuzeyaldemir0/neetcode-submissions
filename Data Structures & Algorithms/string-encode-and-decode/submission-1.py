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
                for _ in range(str_len):
                    new_str += s[i]
                    i += 1
                res.append(new_str)
                count = ""
        return res