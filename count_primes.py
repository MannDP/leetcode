from math import ceil, sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        # base case
        if n < 2:
            return 0

        primes = [False, False] + [True] * (n-2)
        for p in range(2, int(sqrt(n)) + 1):
            if primes[p]:
                # set multiples
                primes[p*p: n: p] = [False] * ceil(n / p - p)
        return sum(primes)


s = Solution()
print(s.countPrimes(10))
print(s.countPrimes(0))
print(s.countPrimes(1))
