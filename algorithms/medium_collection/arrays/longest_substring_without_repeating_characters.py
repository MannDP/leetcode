class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                chars[ord(s[left])] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res


    def mySolution(self, s: str) -> int:
        char_idx = {}

        # state tracking
        start_ptr = 0
        end_ptr = 0
        max_len = 0

        while end_ptr < len(s):
            char = s[end_ptr]

            if char in char_idx:
                # move index forward
                next_start_ptr = char_idx[char] + 1
                
                # evict map entries
                while start_ptr < next_start_ptr:
                    char_idx.pop(s[start_ptr])
                    start_ptr += 1
            else:
                # update map
                char_idx[char] = end_ptr
                # expand current string
                max_len = max(max_len, end_ptr - start_ptr + 1)
                end_ptr += 1
        
        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("abcdefghijk"))
