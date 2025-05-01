class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        curr = ''
        curr_len = 0
        maxLen = 0
        i = 0
        while i < len(s):
            if s[i] not in curr:
                curr += s[i]
                curr_len += 1
                i += 1
                if curr_len > maxLen:
                    maxLen = curr_len
            else:
                i = i - curr_len + 1
                curr = ''
                curr_len = 0
        return maxLen
