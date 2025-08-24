class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        if m * k > n:
            return -1

        def ok(day):
            bouquets = consec = 0
            for x in arr:
                if x <= day:
                    consec += 1
                    if consec == k:
                        bouquets += 1
                        consec = 0
                else:
                    consec = 0
            return bouquets >= m

        lo, hi = min(arr), max(arr)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
