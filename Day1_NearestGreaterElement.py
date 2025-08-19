from bisect import bisect_left  

class Solution:
    def farMin(self, arr):
        n = len(arr)
       
        pairs = sorted((val, i) for i, val in enumerate(arr))

       
        pref = [0]*n
        mx = -1
        for k, (_, idx) in enumerate(pairs):
            if idx > mx:
                mx = idx
            pref[k] = mx

        ans = [-1]*n
        for i, v in enumerate(arr):
      
            pos = bisect_left(pairs, (v, -1))
            if pos > 0:
                j = pref[pos-1]  
                if j > i:
                    ans[i] = j
        return ans
