from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return ""
        
        freq_p = Counter(p)
        freq_s = {}
        
        required = len(freq_p)
        formed = 0
        l, r = 0, 0
        min_len = float("inf")
        min_window = (0, 0)
        
        while r < len(s):
            char = s[r]
            freq_s[char] = freq_s.get(char, 0) + 1
            
            if char in freq_p and freq_s[char] == freq_p[char]:
                formed += 1
            
            while l <= r and formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)
                
                freq_s[s[l]] -= 1
                if s[l] in freq_p and freq_s[s[l]] < freq_p[s[l]]:
                    formed -= 1
                l += 1
            
            r += 1
        
        if min_len == float("inf"):
            return ""
        else:
            return s[min_window[0]:min_window[1] + 1]
            
