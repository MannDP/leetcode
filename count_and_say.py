class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        digit_string = self.countAndSay(n-1)

        # say digit string
        digits = []
        counts = []

        digit = digit_string[0]
        count = 1
        for i in range(1, len(digit_string)):
            c = digit_string[i]
            if c == digit:
                count += 1
            else:
                digits.append(digit)
                counts.append(count)

                count = 1
                digit = c

        if count:
            digits.append(digit)
            counts.append(count)

        # convert to number
        result = ""
        for i in range(len(digits)):
            digit = digits[i]
            count = counts[i]
            result += str(count)
            result += digit
        return result
