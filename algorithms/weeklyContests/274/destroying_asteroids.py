from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True

s = Solution()
print(s.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))
print(s.asteroidsDestroyed(5, [4,9,23,4]))
