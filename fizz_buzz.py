from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()
        for i in range(1, n + 1):
            div_3 = i % 3 == 0
            div_5 = i % 5 == 0
            if div_3 and div_5:
                result.append("FizzBuzz")
            elif div_3:
                result.append("Fizz")
            elif div_5:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
