class Solution:
    def searchMatrix(self, mat, x):
        if not mat or not mat[0]:
            return False

        n, m = len(mat), len(mat[0])
        lo, hi = 0, n*m - 1

        def val(k):
            return mat[k // m][k % m]

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_val = val(mid)

            if mid_val == x:
                return True

            if val(lo) <= mid_val:
                if val(lo) <= x < mid_val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if mid_val < x <= val(hi):
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
