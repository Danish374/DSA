class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        count = Counter(x % value for x in nums)
        
        i = 0
        while True:
            r = i % value
            if count[r] == 0:
                return i
            count[r] -= 1
            i += 1
