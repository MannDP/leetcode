from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            while stack:
                top = stack[-1]
                if top * asteroid > 0 or top < 0 and asteroid > 0:  # no collision
                    stack.append(asteroid)
                    break
                # collision cases
                if abs(top) == abs(asteroid):  # both explode
                    stack.pop()
                    break
                if abs(asteroid) > abs(top):  # smaller one explodes
                    stack.pop()
                    if not stack:
                        stack.append(asteroid)
                        break
                else:
                    break  # asteroid explodes
        return stack
