class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.oneWay(')', s, range(len(s))) and self.oneWay('(', s, range(len(s)-1, -1, -1))

    def oneWay(self, closing_char: str, s: str, indices) -> bool:
        open_count = 0
        for i in indices:
            if s[i] == closing_char:
                open_count -= 1
                if open_count < 0:
                    return False
            else:
                open_count += 1
        return True
