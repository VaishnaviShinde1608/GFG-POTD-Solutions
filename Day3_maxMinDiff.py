class Solution:
    def maxMinDiff(self, arr, k): 
        if k <= 1:
            return 0

        arr.sort()

        def can(d):
            count = 1
            last = arr[0]
            for x in arr[1:]:
                if x - last >= d:
                    count += 1
                    last = x
                    if count == k:
                        return True
            return False

        lo, hi = 0, arr[-1] - arr[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
