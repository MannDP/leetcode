class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        val = 0
        prev = ''
        for c in s:
            both = prev + c
            if not prev:
                val += numerals[c]
            elif both in numerals:
                delta = numerals[both]
                val += delta - numerals[prev]
            prev = c
        return val



s = Solution()
assert(s.romanToInt("I") == 1)
assert(s.romanToInt("V") == 5)
assert(s.romanToInt("X") == 10)
assert(s.romanToInt("L") == 50)
assert(s.romanToInt("C") == 100)
assert(s.romanToInt("D") == 500)
assert(s.romanToInt("M") == 1000)

assert(s.romanToInt("III") == 3)
assert(s.romanToInt("LVIII") == 58)
assert(s.romanToInt("MCMXCIV") == 1994)
