class Solution:
    def maximizeMedian(self, arr, k):
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            i = n // 2
            level = arr[i]
            cnt = 1
            while i < n - 1 and k > 0:
                diff = arr[i + 1] - level
                need = diff * cnt
                if need <= k:
                    level += diff
                    k -= need
                    i += 1
                    cnt += 1
                else:
                    level += k // cnt
                    k = 0
            if k > 0:
                level += k // cnt
            return level
        else:
            r = n // 2
            l = r - 1
            d = arr[r] - arr[l]
            if k <= d:
                return (arr[l] + arr[r] + k) // 2
            k -= d
            level = arr[r]
            cnt = 2
            i = r
            while i < n - 1 and k > 0:
                diff = arr[i + 1] - level
                need = diff * cnt
                if need <= k:
                    level += diff
                    k -= need
                    i += 1
                    cnt += 1
                else:
                    level += k // cnt
                    k = 0
            if k > 0:
                level += k // cnt
            return level
            
