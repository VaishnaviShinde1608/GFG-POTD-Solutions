class Solution:
    def solve(self, bt):
        bt.sort()
        n = len(bt)
        waiting_time = 0
        total = 0
        
        for i in range(n - 1):
            waiting_time += bt[i]
            total += waiting_time
        
        return total // n
