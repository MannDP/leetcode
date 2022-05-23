class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = right = 0

        locations = {}
        while right < len(s):
            char = s[right]
            last_location = locations.get(char, -1)
            left = max(left, last_location + 1)

            locations[char] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len





# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
