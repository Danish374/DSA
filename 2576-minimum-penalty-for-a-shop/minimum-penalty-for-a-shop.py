class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = customers.count('Y')
        best = penalty
        ans = 0
        
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < best:
                best = penalty
                ans = i + 1
        
        return ans
