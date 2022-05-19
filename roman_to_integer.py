class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000,
        }

        doubles = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        total = 0
        chars = list(s)
        i = 0
        while i < len(chars):
            char = chars[i]
            next = '' if i == len(chars) - 1 else chars[i + 1]
            
            value = symbol_value[char]
            double_key = f'{char}{next}'
            if double_key in doubles:
                value = doubles.get(double_key)
                i += 1
            
            total += value
            
            i += 1
        return total


s = Solution()
# print(s.romanToInt("III"))
# print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
