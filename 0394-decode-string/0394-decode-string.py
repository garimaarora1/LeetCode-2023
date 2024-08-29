class Solution:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:
        result = []
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():
                result.append(s[self.index])
                self.index += 1
            else:
                k = 0
                # build k while the next character is a digit
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1
                # ignore the opening bracket '['
                self.index += 1
                decoded_string = self.decodeString(s)
                # ignore the closing bracket ']'
                self.index += 1
                # build k[decoded_string] and append to the result
                result.append(decoded_string * k)
        return ''.join(result)